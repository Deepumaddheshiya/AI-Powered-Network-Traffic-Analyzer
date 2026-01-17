# 🚨 AI-Powered Network Traffic Analyzer
### Cyber Security | Machine Learning | Intrusion Detection System

<img width="1199" height="750" alt="image" src="https://github.com/user-attachments/assets/e5de9685-283d-4ef9-aa90-2d2eb71bbb4b" />

## 📌 Project Description

**AI-Powered Network Traffic Analyzer** is a **Cyber Security project** that detects **malicious (attack) network traffic** and differentiates it from **normal traffic** using **Machine Learning and Explainable AI (XAI)**.

The system analyzes network traffic data (PCAP files), predicts whether the traffic is **NORMAL or ATTACK**, shows **risk level**, **confidence score**, **visual charts**, and generates a **downloadable PDF security report**.

## 🎯 Features

- ✅ Normal vs Attack traffic detection  
- 🧠 Machine Learning based classification  
- 🔍 Explainable AI (Why attack happened?)  
- 📊 Interactive dashboard with charts  
- 🔐 Risk level analysis (LOW / MEDIUM / HIGH)  
- 📄 Auto-generated Security Report (PDF)  
- 🌐 Flask-based web interface  

## 🧠 Technologies Used

- Python
- Flask
- Machine Learning (Random Forest)
- NFStreamer (optional)
- HTML, CSS, JavaScript
- Chart.js
- ReportLab (PDF generation)


## 📂 Project Structure
<img width="538" height="792" alt="image" src="https://github.com/user-attachments/assets/9c109b34-e090-4de3-b9af-d9b3d4c10130" />


## 📊 Traffic Examples

### ✅ Normal Traffic
- Low packet count
- Normal data flow
- LOW risk
- Verdict: **NORMAL**

<img width="1050" height="921" alt="image" src="https://github.com/user-attachments/assets/944cea60-4d19-445f-93ea-f4b38d8257fd" />


### 🚨 Attack Traffic
- High packet rate
- Abnormal data volume
- HIGH risk
- Verdict: **ATTACK**

<img width="952" height="921" alt="image" src="https://github.com/user-attachments/assets/3bec2966-cd3e-468a-8ec5-ddfca69bbc36" />


## 🧠 Explainable AI (XAI)

The system explains **why traffic is classified as attack**:
- Unusually high data volume
- Abnormal packet rate
- Long connection duration

This improves **trust and transparency**.


## 🔐 Risk Levels

| Risk | Description |
|----|-----------|
| LOW | Safe traffic |
| MEDIUM | Suspicious activity |
| HIGH | Malicious attack |


## 📄 Security Report (PDF)

Generated report includes:
- File name
- Final verdict
- Risk level
- Confidence score
- Explainable AI reasons


## ▶️ How to Run

### Install Dependencies
```bash
pip install -r requirements.txt


