# 🛡️ Cyber Complaint Assistant — 1930 Helpline Tool

A web tool for **Rajasthan Police 1930 Helpline officers** to instantly analyze cybercrime complaints 
in **Hindi, English, or Hinglish** and get structured legal + procedural guidance.

---

## ⚡ Setup in 5 Minutes

### Step 1 — Get a Free Gemini API Key
1. Go to: **https://aistudio.google.com/app/apikey**
2. Sign in with any Google account
3. Click **"Create API Key"**
4. Copy the key (starts with `AIza...`)

---

### Step 2 — Install Python Dependencies

Open terminal in this folder and run:

```bash
pip install streamlit google-generativeai
```

---

### Step 3 — Add Your API Key

Create a folder called `.streamlit` inside your project folder.  
Inside it, create a file called `secrets.toml`:

```
your-project-folder/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml        ← create this
```

Inside `secrets.toml`, paste:

```toml
GEMINI_API_KEY = "AIzaSy...your-key-here"
```

---

### Step 4 — Run Locally

```bash
streamlit run app.py
```

Open your browser at: **http://localhost:8501**  
That's it. The tool is live.

---

## 🌐 Deploy to Streamlit Cloud (Free Public URL)

### Step 1 — Push to GitHub
1. Create a free account at **github.com**
2. Create a new repository (e.g. `cyber-complaint-assistant`)
3. Upload `app.py` and `requirements.txt` to it

### Step 2 — Deploy on Streamlit Cloud
1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository → `app.py` → Deploy

### Step 3 — Add Secret on Streamlit Cloud
1. In your deployed app dashboard → **Settings** → **Secrets**
2. Paste:
```toml
GEMINI_API_KEY = "AIzaSy...your-key-here"
```
3. Save → App restarts → Done!

Your public URL will be something like:  
👉 `https://aaditya-cyber-assistant.streamlit.app`

---

## 🔍 What the Tool Does

| Officer types... | Tool outputs... |
|---|---|
| Hindi / Hinglish / English complaint | Crime category & subcategory |
| "victim ne paytm pe paise bhej diye" | Applicable IT Act sections |
| "OTP share kiya, account khali hua" | IPC + BNSS sections (new criminal code) |
| Any cyber fraud description | Evidence checklist for victim |
| | Which authority to escalate to |
| | Immediate steps for victim |
| | Script: what to say to victim right now |

---

## 📋 Example Inputs That Work

```
Victim ne paytm pe 15000 bhej diye ek fake customer care number pe. Transaction kal hui thi.
```
```
Ladki ki private photos lekar ek unknown number blackmail kar raha hai WhatsApp pe.
```
```
OTP share kiya tha, uske baad account se 45000 cut gaye. SBI account hai.
```
```
Facebook pe fake profile bana ke meri company ke naam se logo se paise maang rahe hain.
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend/UI | Streamlit (Python) |
| AI Model | Google Gemini 1.5 Flash (Free tier) |
| Language | Python 3.9+ |
| Deployment | Streamlit Cloud (free) |
| Cost | ₹0 |

---

## ⚠️ Disclaimer

This tool is an **internship project / prototype** built to assist officers.  
All legal sections and guidance should be verified with a qualified legal officer before taking official action.  
Not intended as a replacement for official NCRP systems.

---

*Built during Rajasthan Police Cyber Cell Internship*
