<h1 align="center"><b>🛡️ AI Log Guard</b></h1>

<h3 align="center" style="color:#36BCF7;">
  Intelligent Anomaly Detection & Automated Threat Response System
</h3>

<p align="center">
  🔐 <b>AI-Powered Security</b> &nbsp;&bull;&nbsp; 📊 <b>Real-Time Monitoring</b> &nbsp;&bull;&nbsp; ⚡ <b>Automated Response</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13.7-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Algorithm-Isolation%20Forest-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Gemini%202.0%20Flash-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" />
</p>

<hr style="border:1px solid #36BCF7; width:60%; margin:auto;" />


## 📖 Project Abstract

**AI Log Guard** is an advanced cybersecurity platform that transforms raw system logs into **actionable security intelligence**.  
Unlike traditional rule-based monitoring tools, it uses a **hybrid AI approach** capable of detecting **zero-day exploits, insider threats, and evolving attack patterns** in real time.

Developed as a **Final Year Project (FYP)** at **COMSATS University Islamabad**, this project combines **machine learning, large language models (LLMs), and automated incident response** into a unified security solution.

---

## 🎬 Demo

<p align="center">
  <img src="FYP Project/assets/video.gif" alt="AI Log Guard Demo" width="700"/>
</p>

<p align="center">
  <em>Real-time log monitoring, anomaly detection, and automated response in action</em>
</p>

---

## 📸 Screenshots

| Dashboard | live Monitor | Anomaly Report | Threat Intel |
|------------|-----------|----------------|----------------|
| <img src="FYP Project/assets/Screenshot1.png" alt="Login Page" width="300"/> | <img src="FYP Project/assets/Screenshot2.png" alt="Dashboard" width="300"/> | <img src="FYP Project/assets/Screenshot (33).png" alt="Anomaly Report" width="300"/> |<img src="FYP Project/assets/Screenshot (32).png" alt="Threat Intel" width="300"/> |


---

## ✨ Key Innovations

### 🧠 Hybrid Detection Engine
- Combines **Isolation Forest (unsupervised anomaly detection)** with **TF-IDF vectorization**.
- Detects statistical deviations **without labeled datasets**.
- Highly effective against unknown and evolving threats.

### 🕵️ LLM-Driven Forensic Intelligence
- Integrates **Gemini 2.0 Flash** via **OpenRouter API**.
- Converts anomaly scores into:
  - Human-readable explanations
  - Attack summaries
  - Step-by-step remediation guidance
- Solves the *“black-box AI”* problem for security analysts.

### ⚡ Real-Time Automated Response
- Multi-threaded Python architecture with **sub-second latency**.
- Supports automated mitigation actions, including:
  - IP blocking
  - Alert generation
  - Incident logging

---

## 🛠️ Technical Architecture

| Layer | Technology |
|-------|-----------|
| **Frontend** | CustomTkinter (Modern, Dark-Mode UI) |
| **Analysis Engine** | Scikit-learn, Pandas, NumPy |
| **ML Algorithms** | Isolation Forest, TF-IDF |
| **LLM Intelligence** | Gemini 2.0 Flash (OpenRouter API) |
| **Threat Intelligence** | IP-API.com |
| **Persistence** | SQLite (Thread-Safe Singleton Pattern) |
| **Concurrency** | Python Multithreading |

---

## 🏗️ System Workflow

```mermaid
graph TD
    A[Raw System Logs]:::input --> B[Log Parsing & Normalization]:::process
    B --> C[TF-IDF Feature Extraction]:::process
    C --> D[Isolation Forest Anomaly Detection]:::process
    D --> E{Anomalous?}:::decision
    E -- Yes --> F[Severity Classification]:::process
    F --> G[LLM Forensic Analysis]:::process
    G --> H[Automated Response & Reporting]:::output
    E -- No --> I[Historical Persistence]:::output

    %% Professional Color Palette Styles
    classDef input fill:#1a1b26,stroke:#7aa2f7,stroke-width:2px,color:#7aa2f7;
    classDef process fill:#24283b,stroke:#414868,stroke-width:1px,color:#c0caf5;
    classDef decision fill:#3b4261,stroke:#e0af68,stroke-width:2px,color:#e0af68;
    classDef output fill:#16161e,stroke:#9ece6a,stroke-width:1px,color:#9ece6a;

```


---

## 📁 Project Structure
```text
FYP PROJECT
├── 🎨 assets/             # Branding, high-DPI UI icons, and demo media  
├── 💾 backups/            # Local data recovery and log archives  
├── ⚡ cache/              # Temporary buffers and IP reputation cache  
├── ⚙️ config/             # Environment variables and API configurations  
├── 📊 data/               # Input log datasets (Simulated & Real-world)  
├── 📜 reports/            # Generated security audits (PDF & CSV)  
│
├── 🧠 src/  
│   ├── 🛠️ backend/  
│   │   ├── core_logic.py      # The "Brain": Anomaly detection & rule execution  
│   │   ├── database_mgr.py    # Singleton SQLite transaction manager  
│   │   └── llm_service.py     # Gemini 2.0 forensic analysis engine  
│   │
│   ├── 🎮 controller/  
│   │   └── main.py            # Application controller & page navigation  
│   │
│   ├── 🖥️ ui/  
│   │   ├── components/        # Custom modern themed widgets  
│   │   └── pages/             # Dashboard, Live Monitor, and Forensic views  
│   │
│   └── 🔧 utils/              # Helper functions for regex and normalization  
│
├── 🌍 config.py               # Global system constants  
├── 🛡️ AiLogGuard.py           # Main Application Entry Point  
└── 📄 README.md               # Documentation & Project Sentinel
```

## 🚀 Getting Started

### Prerequisites
- Python **3.8+** (Tested on **3.13.7**)
- OpenRouter API Key (for LLM forensic analysis)

### Installation
```bash
# Clone the repository
git clone [https://github.com/MohsinHaiderSultan/AI-Log-Guard.git](https://github.com/MohsinHaiderSultan/AI-Log-Guard.git)

# Navigate to project
cd "FYP Project"

# Install requirements
pip install -r requirements.txt

# Run the system
python AiLogGuard.py
```
---

## 🧪 Machine Learning Methodology

**Feature Engineering**
- TF-IDF vectorization of log messages
- Temporal and statistical features

**Detection Strategy**
- Unsupervised anomaly detection (Isolation Forest)
- Adaptive thresholding

**Output**
- Normal vs Anomalous classification
- Severity scoring
- Natural-language forensic explanation

---

## 🔮 Future Enhancements

- Deep learning–based detection models (LSTM, Autoencoders)
- Real-time log streaming (Kafka / Syslog)
- Web-based Security Operations Center (SOC) dashboard
- SIEM platform integration
- Alerting via Email, Slack, and SMS
- Cloud-scale log ingestion and analysis

---

## 👨‍💻 Author

<table align="center">
  <tr>
    <!-- LEFT: PROFILE CARD -->
    <td align="center" width="180">
      <a href="https://github.com/MohsinHaiderSultan">
        <img src="https://github.com/MohsinHaiderSultan.png?size=120"
             width="120"
             style="border-radius:50%; border: 3px solid #36BCF7; padding:2px;"
             alt="Mohsin Haider Sultan"/>
        <br /><br />
        <sub><b>Mohsin Haider Sultan</b></sub>
      </a>
      <br /><br />
      <img src="https://img.shields.io/badge/Project%20Lead-AI%20%26%20Cybersecurity-36BCF7?style=flat-square&logo=probot&logoColor=white" />
    </td>
    <!-- RIGHT: CONTACT + CTA -->
    <td align="center" width="420">
      <p>
        <b style="font-size:16px;">🚀 Connect with the Project Lead</b><br/>
        <sub>AI • Cybersecurity • Research • Development</sub>
      </p>
      <br/>
      <table align="center">
        <tr>
          <td align="center" width="65">
            <a href="https://www.linkedin.com/in/mohsin-haider-sultan-498b5b251">
              <img src="https://www.readmecodegen.com/api/social-icon?name=linkedin&shape=circle&theme=brand"
                   width="38" height="38" alt="LinkedIn"/>
            </a>
          </td>
          <td align="center" width="65">
            <a href="mailto:mohsinhaidersultan001@gmail.com">
              <img src="https://www.readmecodegen.com/api/social-icon?name=gmail&shape=circle&theme=brand"
                   width="38" height="38" alt="Gmail"/>
            </a>
          </td>
          <td align="center" width="65">
            <a href="https://instagram.com/mohsin_haider_sultan_gilgiti">
              <img src="https://www.readmecodegen.com/api/social-icon?name=instagram&shape=circle&theme=brand"
                   width="38" height="38" alt="Instagram"/>
            </a>
          </td>
          <td align="center" width="65">
            <a href="https://mohsinhaidersultan.github.io/Portfolio/">
              <img src="https://img.icons8.com/ios-filled/100/36BCF7/user-male-circle.png"
                   width="38" height="38" alt="Portfolio"/>
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Developed%20at-COMSATS%20University%20Islamabad%20(Sahiwal)-004C97?style=for-the-badge&logo=google-classroom&logoColor=white" />
  <br /><br />
  <img src="https://img.shields.io/badge/%C2%A9%202026-Mohsin%20Haider%20Sultan%20%26%20Team-1a1b26?style=flat-square&logo=github&logoColor=white" />
  <br />
</p>

