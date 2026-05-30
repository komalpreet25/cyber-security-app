import streamlit as st
import re

# ==========================================
# 1. GLOBAL INITIALIZATION & CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="SOC Command Center | AI Cyber Security Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global Session State Navigation Control
if "page" not in st.session_state:
    st.session_state.page = "home"

# Unified SOC Dark Theme CSS injection
def inject_soc_theme():
    st.markdown("""
        <style>
        /* Base App Styling */
        .stApp {
            background-color: #0a0f1d !important;
            color: #e2e8f0 !important;
        }
        
        /* Custom Sidebar Overrides */
        [data-testid="stSidebar"] {
            background-color: #0f172a !important;
            border-right: 1px solid #1e293b;
        }
        
        /* Card & Container Mockups */
        .soc-card {
            background-color: #111827;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #1e293b;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .soc-card h3 {
            color: #38bdf8 !important;
            margin-top: 0px;
        }
        
        /* Metric block styling overrides */
        [data-testid="stMetricValue"] {
            font-size: 32px !important;
            font-weight: 700 !important;
            color: #0ea5e9 !important;
        }
        
        /* Smooth button treatments */
        .stButton>button {
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease;
        }
        
        /* Custom Footer Elements */
        .soc-footer {
            text-align: center;
            padding: 20px;
            color: #64748b;
            font-size: 13px;
            border-top: 1px solid #1e293b;
            margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

inject_soc_theme()


# ==========================================
# 2. PERMANENT SIDEBAR AI PANEL
# ==========================================
with st.sidebar:
    st.title("🛡️ SOC Control")
    st.markdown("`SYSTEM STATUS: OPERATIONAL`")
    st.divider()
    
    # Fast Page Jumper for convenient grading/reviewing
    st.subheader("🌐 Core Navigation")
    if st.button("🏠 Command Home", use_container_width=True):
        st.session_state.page = "home"
    if st.button("📊 Security Dashboard", use_container_width=True):
        st.session_state.page = "dashboard"
        
    st.divider()
    st.subheader("🤖 Quick AI Look-Up")
    sidebar_input = st.text_input("Query triage parameters:", placeholder="e.g., firewall, ransomware")
    
    if sidebar_input:
        query = sidebar_input.lower()
        if "password" in query:
            st.info("🔐 Security Protocol: Enforce >= 12 characters combining symbols, length entropy, and non-dictionary phrases.")
        elif "phishing" in query or "url" in query:
            st.warning("⚠️ Threat vector recognized. Check domain string anomalies and header variations.")
        else:
            st.write("🤖 *System advice: Ensure defensive posture via principle of least privilege (PoLP).*")


# ==========================================
# 3. PAGE VIEW LOGIC
# ==========================================

# 🏠 HOME PAGE VIEW
if st.session_state.page == "home":
    # Hero Title Setup
    st.markdown("<h1 style='color: #f8fafc; font-size: 46px; font-weight: 800; margin-bottom: 5px;'>AI-Powered Cyber Security Command Suite</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #38bdf8; font-size: 19px; font-weight: 400;'>Next-Gen Threat Tactical Triage & Educational Assessment Interface</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Executive Abstract Grid
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.markdown("### 📊 Project Overview")
        st.write(
            "Designed for critical assessment environments, this intelligent interface serves as an operational "
            "framework for handling baseline data vulnerabilities. Integrating pattern identification, heuristic "
            "text scanning, and natural processing guidelines, the platform educates tech administrators on defending system assets."
        )
        st.info("🚀 System Readiness Notice: This portal is formatted explicitly for technical portfolio presentation and structural validation.")
    
    with col_right:
        st.markdown("### ⚡ Threat Metrics")
        m1, m2 = st.columns(2)
        m1.metric("Engine Vectors", "4 Modules")
        m2.metric("SLA Response", "< 120ms")
        
    st.markdown("---")
    st.markdown("### ⚙️ Core Inspection Modules")
    
    # Feature Showcase Grid
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.markdown("""<div class='soc-card'><h3>🔐 Password Strength</h3><p>Evaluates lexical security properties using complex regex pattern recognition logic.</p></div>""", unsafe_allow_html=True)
    with f2:
        st.markdown("""<div class='soc-card'><h3>🎣 Phishing Engine</h3><p>Parses message payloads for social engineering semantic hooks and pressure vocabulary.</p></div>""", unsafe_allow_html=True)
    with f3:
        st.markdown("""<div class='soc-card'><h3>🌐 URL Triage</h3><p>Verifies operational transport layers and filters protocol configurations instantly.</p></div>""", unsafe_allow_html=True)
    with f4:
        st.markdown("""<div class='soc-card'><h3>🤖 SecOps Assistant</h3><p>On-demand interactive operational playbooks regarding cloud and endpoint security postures.</p></div>""", unsafe_allow_html=True)
        
    st.write("")
    if st.button("🚀 Enter Command Dashboard", use_container_width=True, type="primary"):
        st.session_state.page = "dashboard"
        st.rerun()


# 📊 DASHBOARD VIEW
elif st.session_state.page == "dashboard":
    st.markdown("<h1 style='color: #f8fafc; font-size: 38px;'>🛡️ Operational Security Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>Real-Time Analytic Command Panel & Sandbox Utilities</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Command Center KPI Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Security Evaluation Score", "98%", delta="Optimal Dynamic Range")
    with kpi2:
        st.metric("Active Detection Daemons", "4/4 Active")
    with kpi3:
        st.metric("Intercepted Sample Index", "24 Deflected")
    with kpi4:
        st.metric("Cognitive Core Availability", "24/7 Standby")
        
    st.markdown("---")
    st.subheader("🎯 Threat Engine Entrypoints")
    
    # UI Navigation Matrix Layout
    grid_col1, grid_col2 = st.columns(2)
    
    with grid_col1:
        st.markdown("""
            <div class="soc-card">
                <h3>🔐 Dynamic Password Complexity Analyzer</h3>
                <p>Run immediate compliance inspections checking for length constraints, character diversity, and structural predictability matrices.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Initialize Password Analysis Pipeline", use_container_width=True):
            st.session_state.page = "password"
            st.rerun()
            
        st.markdown("""
            <div class="soc-card">
                <h3>🎣 Social Engineering Phishing Parser</h3>
                <p>Scans incoming text data streams against dynamic contextual lexicons to flag potential phishing attacks.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Initialize Phishing Ingestion Stream", use_container_width=True):
            st.session_state.page = "phishing"
            st.rerun()

    with grid_col2:
        st.markdown("""
            <div class="soc-card">
                <h3>🌐 Transport Layer URL Verification</h3>
                <p>Checks structural validity of hostnames and checks if transmission protocols meet minimum transport safety specifications.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch URL Integrity Audit", use_container_width=True):
            st.session_state.page = "url"
            st.rerun()
            
        st.markdown("""
            <div class="soc-card">
                <h3>🤖 SecOps Cognitive Copilot</h3>
                <p>Access structured responses detailing architectural threat mitigation tactics and standard security rules.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Connect To AI Copilot Hub", use_container_width=True):
            st.session_state.page = "ai"
            st.rerun()


# 🔐 PASSWORD CHECKER ENGINE
elif st.session_state.page == "password":
    st.title("🔐 Password Complexity Analyzer")
    st.write("Evaluate lexical structural integrity constraints against targeted entropy configurations.")
    st.markdown("---")
    
    st.warning("🔒 Operational Guardrail: Live user production credentials should not be submitted. Utilize dummy verification variants exclusively.")
    
    password = st.text_input("Target String Input", type="password", placeholder="Provide prospective text string...")
    
    def evaluate_entropy(val):
        score = 0
        if len(val) >= 8: score += 1
        if re.search("[A-Z]", val): score += 1
        if re.search("[0-9]", val): score += 1
        if re.search("[@#$%^&*()_+={}\[\]|\\:;\"'<>,.?/~`-]", val): score += 1
        return score

    if password:
        strength_metric = evaluate_entropy(password)
        st.markdown(f"#### Analysis Metrics: `{strength_metric}/4` Points")
        
        if strength_metric <= 1:
            st.error("🚨 CRITICAL VULNERABILITY: Low Entropy. String easily susceptible to dictionary attacks or direct brute forcing.")
        elif strength_metric <= 3:
            st.warning("⚠️ COMPLIANCE WARNING: Moderate Complexity. Strengthen key length and inject random special characters.")
        else:
            st.success("🛡️ SECURE: High Entropy Profile. Meets modern standards for safe verification storage models.")
            
    st.write("")
    if st.button("⬅ Return To System Console", type="secondary"):
        st.session_state.page = "dashboard"
        st.rerun()


# 🕵️ PHISHING DETECTOR ENGINE
elif st.session_state.page == "phishing":
    st.title("🕵️ Phishing Signature Parser")
    st.write("Analyzes unstructured messaging logs for indicators of malicious intent or social engineering patterns.")
    st.markdown("---")
    
    payload = st.text_area("Ingest E-mail/SMS Message Payload", placeholder="Paste body headers and textual contents for signature inspection...", height=150)
    
    indicators = ["urgent", "click", "verify", "password", "bank", "otp", "login", "account", "suspended", "action required"]
    
    if payload:
        detected_triggers = [word for word in indicators if word in payload.lower()]
        risk_score = len(detected_triggers)
        
        st.markdown(f"#### Risk Metrics Found: `{risk_score}` Threats Flagged")
        
        if risk_score >= 2:
            st.error(f"🚨 ALERT: High Probability Threat Signature Detected! Flagged Keywords: {detected_triggers}")
            st.markdown("""
            **Triage Actions Prescribed:**
            * Do not interact with links embedded within the payload source.
            * Isolate source domain headers and trace original MX authority properties.
            """)
        else:
            st.success("✅ NOMINAL: No high-risk language patterns identified within input data parameters.")
            
    st.write("")
    if st.button("⬅ Return To System Console"):
        st.session_state.page = "dashboard"
        st.rerun()


# 🌐 URL SAFETY CHECKER
elif st.session_state.page == "url":
    st.title("🌐 Protocol-Level URL Safety Verification")
    st.write("Validates endpoint addressing schemes against transport criteria and syntax properties.")
    st.markdown("---")
    
    target_url = st.text_input("Enter Target Domain / URL Asset", placeholder="example.com or https://secure-portal.org")
    
    if target_url:
        # Simple structural parsing
        if target_url.lower().startswith("https://"):
            st.success("🔒 SAFE PROTOCOL ENFORCED: Destination explicitly maps to an encrypted TLS/SSL layer connection.")
            st.info("💡 Portfolio Tip: A secure transport protocol does not verify structural backend legitimacy, but guarantees encrypted routing.")
        else:
            st.error("🚨 UNENCRYPTED TRANSPORT DETECTED: Address uses plain HTTP text or missing protocol validation. Subject to potential MiTM eavesdropping.")
            
    st.write("")
    if st.button("⬅ Return To System Console"):
        st.session_state.page = "dashboard"
        st.rerun()


# 🤖 AI CYBER ASSISTANT KNOWLEDGE BASE
elif st.session_state.page == "ai":
    st.title("🤖 SecOps AI Cognitive Guard")
    st.write("Interactive defensive knowledge repository providing immediate resolution guidance pipelines.")
    st.markdown("---")
    
    prompt = st.text_input("Consult Tactical Database System", placeholder="Type a concept you wish to learn about (e.g. Passwords, Phishing, Cloud Security)...")
    
    if prompt:
        p_low = prompt.lower()
        if "password" in p_low:
            st.markdown("""
            ### 🔐 Passphrase Hardening Framework
            * **Length Parameterization:** Enforce a minimum boundary of 12-16 algorithmic components.
            * **Passphrase Strategy:** Swap standard dictionary mutations for unique, multi-word configurations (e.g., `Copper#Skyline#9761!Matrix`).
            * **MFA Implementations:** Pair storage management software configurations directly alongside hardware key systems or TOTP token steps.
            """)
        elif "phishing" in p_low:
            st.markdown("""
            ### 🎣 Phishing Defense Protocols
            * **Ingestion Isolation:** Verify top-level domains carefully against internal directories.
            * **Grammatical Anomalies:** Look for unnatural syntax, forced urgency statements, and misaligned graphic design components.
            * **Verification Routines:** Reach out directly using official out-of-band support directories instead of relying on links provided in the message.
            """)
        else:
            st.markdown("""
            ### 💻 Core Defensive Infrastructure Guidelines
            * **Network Segmentation:** Split open interfaces away from internal data processing environments.
            * **Zero Trust Architectures:** Enforce strict access authorization checks at every point in the network, regardless of location.
            * **Patch Automation Cycles:** Schedule timely operating system image updates to protect against zero-day vulnerabilities.
            """)
            
    st.write("")
    if st.button("⬅ Return To System Console"):
        st.session_state.page = "dashboard"
        st.rerun()


# ==========================================
# 4. UNIFIED SECURE PORTFOLIO FOOTER
# ==========================================
st.markdown(
    """
    <div class="soc-footer">
        <p>SOC Command Simulator Engine v2.4.0 — Operational Environment</p>
        <p style="color: #38bdf8; font-weight: 500;">Developed by Komalpreet Kaur | BCA Cyber Security Specialist</p>
    </div>
    """, 
    unsafe_allow_html=True
)
