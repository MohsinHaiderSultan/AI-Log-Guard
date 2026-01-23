import os
import json
import requests
from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field
from openai import OpenAI 

# Import configuration from your config.py
from config import LLM_API_KEY, LLM_MODEL_NAME, LLM_PROMPT_TEMPLATE_PATH

# ==============================================================================
# 1. Pydantic Data Models (The "Schema") - EXPORTED
# ==============================================================================

# NOTE: These classes are defined at the top-level so they can be imported
# by other modules, like core_logic.py, which uses them for type hinting.

class SeverityLevel(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

class AttackType(str, Enum):
    BRUTE_FORCE = "BRUTE_FORCE"
    SQL_INJECTION = "SQL_INJECTION"
    XSS = "XSS"
    COMMAND_INJECTION = "COMMAND_INJECTION"
    UNKNOWN = "UNKNOWN"

class LogID(BaseModel):
    log_id: str = Field(description="The unique ID extracted from the log line (e.g., LOGID-001)")

class IPAddress(BaseModel):
    ip_address: str = Field(description="IPv4 address found in the log")

class ResponseCode(BaseModel):
    response_code: str = Field(description="HTTP response status code or System Event ID")

class WebTrafficPattern(BaseModel):
    url_path: str
    http_method: str
    hits_count: int
    response_codes: Dict[str, int]
    unique_ips: int

class WebSecurityEvent(BaseModel):
    relevant_log_entry_ids: List[LogID] = Field(default_factory=list)
    reasoning: str
    event_type: str
    severity: SeverityLevel
    confidence_score: float
    url_pattern: str
    http_method: str
    source_ips: List[IPAddress] = Field(default_factory=list)
    possible_attack_patterns: List[AttackType] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)

class LogAnalysis(BaseModel):
    summary: str
    observations: List[str] = Field(default_factory=list)
    planning: List[str] = Field(default_factory=list)
    events: List[WebSecurityEvent] = Field(default_factory=list)
    traffic_patterns: List[WebTrafficPattern] = Field(default_factory=list)
    highest_severity: Optional[SeverityLevel] = SeverityLevel.INFO
    requires_immediate_attention: bool = False


# ==============================================================================
# 2. The AI Service Wrapper
# ==============================================================================

class STRESSED:
    """
    Connects to the Cloud LLM API (OpenRouter) to perform forensic analysis.
    Enforces structured JSON output using Pydantic validation.
    """
    def __init__(self):
        # Initialize the OpenAI Client for OpenRouter
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=LLM_API_KEY,
            default_headers={
                "HTTP-Referer": "https://github.com/AiLogGuard", 
                "X-Title": "AI LogGuard",
            }
        )
        self.model_name = LLM_MODEL_NAME
        
        # Load the Prompt Template
        try:
            # Using an absolute path check to be safer
            template_path = os.path.abspath(LLM_PROMPT_TEMPLATE_PATH) 
            with open(template_path, "r", encoding="utf-8") as f:
                self.prompt_template = f.read()
        except Exception as e:
            print(f"[LLM Service] Error loading prompt template: {e}")
            self.prompt_template = "Analyze these {log_type} logs: {logs}. Schema: {model_schema}"

    def analyze_logs(self, logs: List[str], log_type: str = "Web Server Access Logs") -> LogAnalysis:
        """
        Sends logs to the LLM and returns a structured LogAnalysis object.
        """
        # 1. Pre-process Logs
        chunked_logs = logs[:50] 
        
        log_lines_with_ids = []
        for idx, line in enumerate(chunked_logs):
            log_id = f"LOGID-{idx:03d}" 
            log_lines_with_ids.append(f"[{log_id}] {line}")
            
        logs_text = "\n".join(log_lines_with_ids)

        # 2. Get the JSON Schema from Pydantic
        # model_json_schema is the correct method for pydantic V2+
        json_schema = json.dumps(LogAnalysis.model_json_schema(), indent=2)

        # 3. Fill the Prompt Template
        final_prompt = self.prompt_template.format(
            log_type=log_type, 
            stress_prompt="", 
            logs=logs_text,
            model_schema=json_schema
        )

        try:
            print(f"[LLM Service] Sending request to OpenRouter (Model: {self.model_name}) for {log_type}...")
            
            # 4. Call the API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "system", 
                        "content": f"You are a senior security analyst specializing in {log_type}. You must output valid JSON only, strictly following the provided schema. Do not include markdown formatting or any text outside the JSON object."
                    },
                    {
                        "role": "user", 
                        "content": final_prompt
                    }
                ],
                temperature=0.1, 
                response_format={"type": "json_object"} 
            )

            # 5. Parse Response
            raw_content = response.choices[0].message.content
            print("[LLM Service] Received response.")

            # 6. Clean and Validate
            # Attempt to clean potential markdown wrappers added by the model
            if "```json" in raw_content:
                raw_content = raw_content.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_content:
                raw_content = raw_content.split("```")[1].strip()

            analysis_data = LogAnalysis.model_validate_json(raw_content)
            
            # Calculate and set requires_immediate_attention flag
            # Checks if any event has a CRITICAL or HIGH severity
            if any(e.severity in (SeverityLevel.CRITICAL, SeverityLevel.HIGH) for e in analysis_data.events):
                 analysis_data.requires_immediate_attention = True

            return analysis_data

        except Exception as e:
            print(f"[LLM Service] API or Validation Error: {type(e).__name__}: {e}")
            
            # Return a safe fallback object so the UI doesn't crash
            return LogAnalysis(
                summary=f"Analysis Failed due to API/Validation Error: {type(e).__name__}",
                observations=["Check API Key and Model Name in config.py", "Check Internet Connection", "The model might have returned invalid JSON."], 
                highest_severity=SeverityLevel.INFO
            )

    # --- OPTIONAL: Image Analysis Method (If needed later) ---
    def analyze_image(self, image_url: str, prompt: str = "What is in this image?") -> str:
        # Implementation remains the same
        try:
            try:
                from config import LLM_VISION_MODEL_NAME
                vision_model = LLM_VISION_MODEL_NAME
            except ImportError:
                vision_model = self.model_name

            print(f"[LLM Service] Analyzing image: {image_url}")
            response = self.client.chat.completions.create(
                model=vision_model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": image_url}}
                        ]
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error analyzing image: {str(e)}"


# ==============================================================================
# 3. Service Singleton - EXPORTED
# ==============================================================================

class LLMService:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(LLMService, cls).__new__(cls)
            # Initialize the analyzer instance once
            cls._instance.analyzer = STRESSED()
        return cls._instance

    def get_analyzer(self):
        """Returns the STRESSED instance which contains the LLM client."""
        return self.analyzer

def get_llm_service():
    """
    Public accessor function for the LLMService singleton.
    This is what CoreLogic imports and calls.
    """
    return LLMService()