# 🛡️ Cyber Complaint Assistant — 1930 Helpline Tool

> An AI-powered web tool for Indian police officers manning the **1930 National Cyber Crime Helpline**, built to analyze cybercrime complaints in **Hindi, English, and Hinglish** and instantly generate structured legal + procedural guidance.

---

## 🎯 Problem Statement

Officers at the 1930 helpline handle hundreds of cybercrime complaints daily — most from victims who communicate in **Hindi or Hinglish**. Existing tools like NCRP only support English, and there is no single tool that combines:

- Hinglish language understanding
- Indian cyber law (IT Act 2000 + BNSS 2023)
- 1930 helpline response protocol

This tool was built to bridge that gap, directly inspired by real observations during a **Rajasthan Police Cyber Cell internship**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗣️ Hinglish Support | Understands Hindi, English, and mixed Hinglish input |
| ⚡ Urgency Detection | AUTO flags HIGH / MEDIUM / LOW based on complaint context |
| ⚖️ IT Act Sections | Identifies applicable sections (66C, 66D, 67, 67A, etc.) with reasons |
| 📜 IPC + BNSS Sections | Covers both legacy IPC and new Bharatiya Nyaya Sanhita sections |
| 🔍 Evidence Checklist | Specific items to ask the victim to collect (UTR, screenshots, etc.) |
| 📡 Escalation Guidance | Directs to correct authority — NCRP, IFSO, State CID Cyber |
| 🩺 Victim Guidance | Priority-ordered immediate steps for the victim |
| 📞 Response Script | Exact words the officer should say to the victim right now |

---

## 🧪 Example Inputs

```
Victim ne paytm pe 15000 bhej diye ek fake customer care number pe. Transaction aaj hui.
```
```
Ladki ki private photos lekar ek unknown number WhatsApp pe blackmail kar raha hai.
```
```
OTP share kiya tha, uske baad SBI account se 45000 cut gaye.
```
```
Someone called saying TRAI will disconnect my SIM, took my Aadhaar details.
```
```
Facebook pe fake profile bana ke logo se mere naam pe paise maang rahe hain.
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Python + Streamlit |
| AI Model | LLaMA 3.3 70B via Groq API |
| Deployment | Streamlit Cloud (free) |
| Language Support | Hindi · English · Hinglish |
| Cost | ₹0 |

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/cyber-complaint-assistant
cd cyber-complaint-assistant
```

### 2. Install dependencies
```bash
pip install streamlit groq
```

### 3. Get a free Groq API key
Go to → **https://console.groq.com/keys** → Create API Key → copy it

### 4. Add your API key
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_...your-key-here"
```

### 5. Run
```bash
streamlit run app.py
```
Open **http://localhost:8501**

---

## 🌐 Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to **https://share.streamlit.io** → Sign in with GitHub → New App
3. Select repo → `app.py` → Deploy
4. Go to **Settings → Secrets** and add:
```toml
GROQ_API_KEY = "gsk_...your-key-here"
```
5. Save → your app is live at `yourname-cyber-assistant.streamlit.app`

---

## 📁 Project Structure

```
cyber-complaint-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚖️ Legal Sections Covered

**IT Act 2000**
- 66C — Identity Theft
- 66D — Cheating by impersonation using computer
- 67 — Publishing obscene material
- 67A — Publishing sexually explicit material
- 43 — Unauthorised access / data theft

**BNSS / IPC**
- 318 — Cheating (replaces IPC 420)
- 351 — Criminal intimidation (replaces IPC 506)
- 308 — Extortion (replaces IPC 383)
- 316 — Criminal breach of trust (replaces IPC 406)

---

## 🏛️ Context

Built during an internship at **Rajasthan Police Cyber Cell** as a practical tool to assist 1930 helpline officers. The 1930 helpline is India's national cybercrime reporting number managed by MHA (Ministry of Home Affairs).

---

## ⚠️ Disclaimer

This is an **internship prototype** and educational project. All legal sections and procedural guidance should be verified with a qualified legal officer before taking official action. Not a replacement for official NCRP systems or legal counsel.

---

## 👤 Author

Built during Rajasthan Police Cyber Cell Internship  
Powered by [Groq](https://groq.com) · Deployed on [Streamlit Cloud](https://streamlit.io/cloud)
