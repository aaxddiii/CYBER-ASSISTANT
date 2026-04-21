import streamlit as st
from groq import Groq
import json
import re

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cyber Complaint Assistant — 1930",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0e1a;
    color: #e2e8f0;
}
.stApp { background-color: #0a0e1a; }
.block-container { padding: 2rem 3rem; max-width: 1400px; }

/* ── Header ── */
.header-wrap {
    display: flex; align-items: center; gap: 1.2rem;
    border-bottom: 2px solid #ff9933;
    padding-bottom: 1rem; margin-bottom: 2rem;
}
.header-ashoka {
    font-size: 3.2rem; line-height: 1;
}
.header-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.2rem; font-weight: 700;
    color: #ffffff; letter-spacing: 0.04em;
    line-height: 1.1;
}
.header-sub {
    font-size: 0.8rem; color: #94a3b8;
    letter-spacing: 0.12em; text-transform: uppercase;
    margin-top: 0.2rem;
}
.header-badge {
    margin-left: auto;
    background: linear-gradient(135deg, #ff9933 0%, #ff6600 100%);
    color: #0a0e1a; font-family: 'Rajdhani', sans-serif;
    font-weight: 700; font-size: 1rem;
    padding: 0.4rem 1rem; border-radius: 4px;
    letter-spacing: 0.08em;
}

/* ── Input Section ── */
.input-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.1rem; font-weight: 600;
    color: #94a3b8; letter-spacing: 0.1em;
    text-transform: uppercase; margin-bottom: 0.4rem;
}
.stTextArea textarea {
    background-color: #111827 !important;
    border: 1.5px solid #1e3a5f !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    padding: 1rem !important;
    transition: border-color 0.2s;
}
.stTextArea textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
}
.stTextArea textarea::placeholder { color: #4b5563 !important; }

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    padding: 0.65rem 2.5rem !important;
    transition: all 0.2s !important;
    text-transform: uppercase !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 15px rgba(37,99,235,0.4) !important;
}

/* ── Result Cards ── */
.result-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-top: 1.5rem;
}
.result-card {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 3px; height: 100%;
}
.card-crime::before  { background: #ef4444; }
.card-it::before     { background: #3b82f6; }
.card-ipc::before    { background: #8b5cf6; }
.card-evidence::before { background: #10b981; }
.card-escalate::before { background: #f59e0b; }
.card-victim::before { background: #06b6d4; }
.card-script::before { background: #ff9933; }
.card-full { grid-column: 1 / -1; }

.card-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.75rem; font-weight: 700;
    letter-spacing: 0.15em; text-transform: uppercase;
    color: #64748b; margin-bottom: 0.6rem;
}
.card-main {
    font-size: 1.05rem; font-weight: 600; color: #f1f5f9;
}
.card-sub {
    font-size: 0.85rem; color: #94a3b8; margin-top: 0.2rem;
}
.tag {
    display: inline-block;
    background: #1e293b; border: 1px solid #334155;
    border-radius: 4px; padding: 0.2rem 0.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem; color: #93c5fd;
    margin: 0.2rem 0.2rem 0 0;
}
.tag-ipc { color: #c4b5fd; }
.tag-bnss { color: #6ee7b7; }
.bullet-list {
    list-style: none; padding: 0; margin: 0;
}
.bullet-list li {
    padding: 0.3rem 0 0.3rem 1.2rem;
    position: relative; font-size: 0.9rem; color: #cbd5e1;
    border-bottom: 1px solid #1e293b;
}
.bullet-list li:last-child { border-bottom: none; }
.bullet-list li::before {
    content: '›'; position: absolute; left: 0;
    color: #3b82f6; font-weight: 700; font-size: 1rem;
}
.script-box {
    background: #0f172a;
    border: 1px solid #1e3a5f;
    border-radius: 6px;
    padding: 1rem 1.2rem;
    font-size: 0.9rem; color: #bfdbfe;
    line-height: 1.6;
    font-style: italic;
}
.urgency-HIGH {
    display: inline-block;
    background: #7f1d1d; color: #fca5a5;
    border: 1px solid #ef4444;
    border-radius: 4px; padding: 0.15rem 0.7rem;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem; font-weight: 700;
    letter-spacing: 0.1em;
}
.urgency-MEDIUM {
    display: inline-block;
    background: #78350f; color: #fcd34d;
    border: 1px solid #f59e0b;
    border-radius: 4px; padding: 0.15rem 0.7rem;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem; font-weight: 700;
    letter-spacing: 0.1em;
}
.urgency-LOW {
    display: inline-block;
    background: #064e3b; color: #6ee7b7;
    border: 1px solid #10b981;
    border-radius: 4px; padding: 0.15rem 0.7rem;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem; font-weight: 700;
    letter-spacing: 0.1em;
}
.divider {
    border: none; border-top: 1px solid #1e293b;
    margin: 1.5rem 0;
}
.example-pill {
    display: inline-block;
    background: #0f172a; border: 1px solid #1e3a5f;
    border-radius: 20px; padding: 0.3rem 0.9rem;
    font-size: 0.82rem; color: #64748b;
    margin: 0.2rem; cursor: pointer;
    transition: all 0.15s;
}
.footer-note {
    text-align: center;
    font-size: 0.75rem; color: #374151;
    margin-top: 2rem; padding-top: 1rem;
    border-top: 1px solid #1e293b;
    letter-spacing: 0.05em;
}

/* ── Spinner override ── */
.stSpinner > div { border-top-color: #3b82f6 !important; }

/* ── Selectbox ── */
.stSelectbox > div > div {
    background-color: #111827 !important;
    border: 1.5px solid #1e3a5f !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Header ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
  <div class="header-ashoka">🛡️</div>
  <div>
    <div class="header-title">Cyber Complaint Assistant</div>
    <div class="header-sub">National Cyber Crime Helpline · 1930 · Rajasthan Police</div>
  </div>
  <div class="header-badge">BETA v1.0</div>
</div>
""", unsafe_allow_html=True)

# ─── Gemini Setup ────────────────────────────────────────────────────────────
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    st.error("⚠️  Groq API key not found. Add GROQ_API_KEY to .streamlit/secrets.toml")
    st.stop()

groq_client = Groq(api_key=GROQ_API_KEY)

# ─── Prompt ──────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert legal assistant for Indian police officers manning the 1930 National Cyber Crime Helpline.
You understand Hindi, English, and Hinglish (mixed Hindi-English) fluently.

Analyze the given cyber crime complaint and respond ONLY with a valid JSON object — no preamble, no markdown, no backticks.

Use this EXACT JSON schema:
{
  "crime_category": "Main crime type (e.g. UPI/Payment Fraud)",
  "crime_subcategory": "Specific variant (e.g. Fake Merchant Fraud)",
  "urgency_level": "HIGH or MEDIUM or LOW",
  "it_act_sections": [
    {"section": "66C", "title": "Identity Theft", "why": "one-line reason"}
  ],
  "ipc_sections": [
    {"section": "420", "title": "Cheating", "why": "one-line reason"}
  ],
  "bnss_sections": [
    {"section": "318(4)", "title": "Cheating", "why": "one-line reason"}
  ],
  "evidence_to_collect": [
    "Screenshot of transaction with UTR number",
    "Bank statement showing debit"
  ],
  "escalation_authority": "Which unit / portal to escalate to (e.g. NCRP portal cybercrime.gov.in, IFSO cell, State CID Cyber)",
  "immediate_victim_guidance": [
    "Call bank immediately to freeze account",
    "File complaint on cybercrime.gov.in within 24 hours"
  ],
  "first_response_script": "Exact words the officer should say to the victim right now, in a calm and helpful tone. 2-3 sentences. Can be in Hindi or English based on the language of the complaint."
}

Rules:
- Always include BNSS sections (new criminal code replacing CrPC/IPC, effective July 2024)
- IPC sections are for reference/legacy
- urgency HIGH = financial fraud with recent transaction (freeze window open), sexual crimes, minors involved
- urgency MEDIUM = ongoing harassment, account hacked, data breach
- urgency LOW = old fraud, awareness queries
- evidence_to_collect must be specific and actionable (5-8 items)
- immediate_victim_guidance must be steps in correct priority order (3-5 steps)
- first_response_script must be empathetic and practical
"""

# ─── Analysis Function ───────────────────────────────────────────────────────
def analyze_complaint(complaint_text: str) -> dict:
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Complaint:\n{complaint_text}"}
        ],
        temperature=0.1,
        max_tokens=1500,
    )
    raw = response.choices[0].message.content.strip()
    raw = re.sub(r"^```[a-z]*\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)

# ─── Example Complaints ──────────────────────────────────────────────────────
EXAMPLES = [
    "Victim ne paytm pe 15000 bhej diye ek fake customer care number pe. Transaction kal hui thi.",
    "Ladki ki private photos lekar ek unknown number blackmail kar raha hai WhatsApp pe.",
    "OTP share kiya tha, uske baad account se 45000 cut gaye. SBI account hai.",
    "Facebook pe fake profile bana ke meri company ke naam se logo se paise maang rahe hain.",
    "Someone called pretending to be from TRAI, said my SIM will be disconnected, took my Aadhaar details.",
    "Online job offer mila, 5000 registration fee bhari, ab contact cut kar liya scammer ne.",
]

# ─── Layout ──────────────────────────────────────────────────────────────────
col_input, col_gap, col_output = st.columns([5, 0.3, 6])

with col_input:
    st.markdown('<div class="input-label">Complaint Description</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem; color:#4b5563; margin-bottom:0.6rem;">Hindi · English · Hinglish — sab chalega</div>', unsafe_allow_html=True)

    complaint = st.text_area(
        label="complaint_input",
        label_visibility="collapsed",
        placeholder="Type complaint here...\n\nExample: Victim ne UPI pe paise bhej diye fake number pe, abhi hua hai...",
        height=180,
        key="complaint_box"
    )

    st.markdown("**Quick examples** — click to use:")
    # Show examples as selectable
    selected_example = st.selectbox(
        "Select an example complaint:",
        ["— choose an example —"] + EXAMPLES,
        label_visibility="collapsed",
        key="example_select"
    )
    if selected_example != "— choose an example —":
        st.session_state["prefill"] = selected_example
        st.info(f"📋 Selected: *{selected_example[:60]}...*" if len(selected_example) > 60 else f"📋 Selected: *{selected_example}*")

    use_example = st.button("Use Selected Example", key="use_example", use_container_width=False)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    analyze_btn = st.button("🔍  ANALYZE COMPLAINT", use_container_width=True, key="analyze")

    # Tips
    st.markdown("""
    <div style="margin-top:1.2rem; background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:1rem 1.2rem;">
      <div style="font-family:'Rajdhani',sans-serif; font-size:0.75rem; color:#475569; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:0.5rem;">Tips for best results</div>
      <ul style="margin:0; padding:0 0 0 1rem; font-size:0.82rem; color:#64748b; line-height:1.8;">
        <li>Mention when the incident happened (aaj/kal/1 week ago)</li>
        <li>Include the platform (WhatsApp, UPI, email, Instagram)</li>
        <li>Mention amount lost if financial fraud</li>
        <li>Note if victim already contacted bank</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

# Determine final complaint text
final_complaint = complaint
if use_example and selected_example != "— choose an example —":
    final_complaint = selected_example

# ─── Output ──────────────────────────────────────────────────────────────────
with col_output:
    if analyze_btn or use_example:
        text_to_analyze = final_complaint.strip()
        if not text_to_analyze:
            st.warning("⚠️ Please enter or select a complaint first.")
        else:
            with st.spinner("Analyzing complaint..."):
                try:
                    result = analyze_complaint(text_to_analyze)

                    urgency = result.get("urgency_level", "MEDIUM")
                    crime_cat = result.get("crime_category", "—")
                    crime_sub = result.get("crime_subcategory", "")
                    it_secs = result.get("it_act_sections", [])
                    ipc_secs = result.get("ipc_sections", [])
                    bnss_secs = result.get("bnss_sections", [])
                    evidence = result.get("evidence_to_collect", [])
                    escalation = result.get("escalation_authority", "—")
                    guidance = result.get("immediate_victim_guidance", [])
                    script = result.get("first_response_script", "—")

                    # ── Card 1: Crime + Urgency ──
                    st.markdown(f"""
                    <div class="result-card card-crime">
                      <div class="card-title">Crime Identified</div>
                      <div class="card-main">{crime_cat}</div>
                      <div class="card-sub">{crime_sub}</div>
                      <div style="margin-top:0.6rem;">
                        <span class="urgency-{urgency}">⚡ {urgency} URGENCY</span>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── Cards: IT Act + IPC ──
                    def make_tag(s, css_class):
                        why = s.get("why", "")
                        sec = s.get("section", "")
                        title = s.get("title", "")
                        return f'<span class="{css_class}" title="{why}">§{sec} — {title}</span>'

                    it_tags = "".join([make_tag(s, "tag") for s in it_secs])
                    ipc_tags = "".join([make_tag(s, "tag tag-ipc") for s in ipc_secs])
                    bnss_tags = "".join([make_tag(s, "tag tag-bnss") for s in bnss_secs])

                    cols = st.columns(2)
                    with cols[0]:
                        st.markdown(f"""
                        <div class="result-card card-it">
                          <div class="card-title">IT Act 2000 Sections</div>
                          <div>{it_tags if it_tags else '<span style="color:#4b5563;font-size:0.85rem;">None applicable</span>'}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with cols[1]:
                        st.markdown(f"""
                        <div class="result-card card-ipc">
                          <div class="card-title">IPC / BNSS Sections</div>
                          <div>{ipc_tags}{bnss_tags if (ipc_tags or bnss_tags) else '<span style="color:#4b5563;font-size:0.85rem;">None applicable</span>'}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    # ── Evidence ──
                    evidence_items = "".join([f"<li>{e}</li>" for e in evidence])
                    st.markdown(f"""
                    <div class="result-card card-evidence" style="margin-top:0.8rem;">
                      <div class="card-title">Evidence to Collect from Victim</div>
                      <ul class="bullet-list">{evidence_items}</ul>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── Escalation + Victim Guidance ──
                    guidance_items = "".join([f"<li>{g}</li>" for g in guidance])
                    cols2 = st.columns(2)
                    with cols2[0]:
                        st.markdown(f"""
                        <div class="result-card card-escalate" style="margin-top:0.8rem;">
                          <div class="card-title">Escalate To</div>
                          <div class="card-main" style="font-size:0.95rem;">{escalation}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with cols2[1]:
                        st.markdown(f"""
                        <div class="result-card card-victim" style="margin-top:0.8rem;">
                          <div class="card-title">Immediate Steps for Victim</div>
                          <ul class="bullet-list">{guidance_items}</ul>
                        </div>
                        """, unsafe_allow_html=True)

                    # ── First Response Script ──
                    st.markdown(f"""
                    <div class="result-card card-script" style="margin-top:0.8rem;">
                      <div class="card-title">📞 First Response Script — What to say to the victim NOW</div>
                      <div class="script-box">{script}</div>
                    </div>
                    """, unsafe_allow_html=True)

                except json.JSONDecodeError:
                    st.error("⚠️ Could not parse Gemini response. Try rephrasing the complaint.")
                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")
    else:
        # Placeholder state
        st.markdown("""
        <div style="
          height: 100%;
          min-height: 400px;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          text-align: center;
          border: 2px dashed #1e293b;
          border-radius: 12px;
          padding: 3rem;
        ">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
          <div style="font-family:'Rajdhani',sans-serif; font-size:1.3rem; font-weight:600; color:#475569; letter-spacing:0.05em;">
            Analysis results will appear here
          </div>
          <div style="font-size:0.85rem; color:#374151; margin-top:0.5rem;">
            Enter a complaint on the left and click Analyze
          </div>
        </div>
        """, unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-note">
  Built for 1930 Helpline Officers · Rajasthan Police Cyber Cell Internship Project ·
  Powered by Google Gemini · Not for production use without legal review
</div>
""", unsafe_allow_html=True)
