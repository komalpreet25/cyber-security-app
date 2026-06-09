import streamlit as st
import re
import sqlite3
import pandas as pd

# 1. PAGE CONFIGURATION & THEME
st.set_page_config(
    page_title="Cyber Security Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply consistent dark navy styling across all components
st.markdown("""
    <style>
    /* Dark Navy Background and White Text */
    .stApp {
        background-color: #0d1b2a !important;
        color: #e0e1dd !important;
    }
    /* Sidebar Background styling */
    [data-testid="stSidebar"] {
        background-color: #1b263b !important;
    }
    /* Custom simple styling for Feature Cards */
    .feature-card {
        background-color: #1b263b;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #415a77;
        margin-bottom: 15px;
    }
    .feature-card h3 {
        color: #e0e1dd !important;
        margin-top: 0;
    }
    .feature-card p {
        color: #e0e1dd !important;
        font-size: 14px;
        margin-bottom: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Page Navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Initialize Session State for AI Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# 2. SIDEBAR NAVIGATION
with st.sidebar:
    # High-contrast bright white headings
    st.markdown("<h1 style='color: #FFFFFF; font-weight: 700; margin-bottom: 0px;'>🛡️ Navigation Center</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #E5E7EB; margin-top: 5px;'>Select a module below to test its functionality.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("🏠 Home Page", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
        
    if st.button("📊 Main Dashboard", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()
        
    st.markdown("---")
    st.markdown("<h3 style='color: #FFFFFF; font-weight: 700;'>🛠️ Quick Tools</h3>", unsafe_allow_html=True)
    
    if st.button("Password Checker", use_container_width=True):
        st.session_state.page = "password"
        st.rerun()
    if st.button("Phishing Detector", use_container_width=True):
        st.session_state.page = "phishing"
        st.rerun()
    if st.button("URL Safety Checker", use_container_width=True):
        st.session_state.page = "url"
        st.rerun()
    if st.button("AI Assistant", use_container_width=True):
        st.session_state.page = "ai"
        st.rerun()


# 3. PAGE LOGIC

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.title("🛡️ AI-Powered Cyber Security Assistant")
    st.write("An educational tool designed to analyze common security risks, evaluate password strengths, detect suspicious links, and provide cyber safety guidance.")
    st.markdown("---")
    
    st.subheader("💡 Core Features Available")
    
    # 4 Feature Cards Layout
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>🔐 Password Checker</h3>
                <p>Tests your password strength based on length, numbers, capital letters, and special characters.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("") # Spacing
        st.markdown("""
            <div class="feature-card">
                <h3>🌐 URL Safety Checker</h3>
                <p>Inspects website links to check if they use secure HTTPS protocols and standard domain structures.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3>🎣 Phishing Detector</h3>
                <p>Scans text messages or emails to spot suspicious words commonly used in phishing scams.</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("") # Spacing
        st.markdown("""
            <div class="feature-card">
                <h3>🤖 AI Assistant</h3>
                <p>An interactive guide to answer your basic cyber security questions and offer online safety tips.</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Primary Action Button
    if st.button("🚀 Enter Dashboard", use_container_width=True, type="primary"):
        st.session_state.page = "dashboard"
        st.rerun()

# --- DASHBOARD PAGE ---
elif st.session_state.page == "dashboard":
    # 🚨 FIX PLACED HERE: This keeps your dashboard button labels bright white at all times
    st.markdown("""
        <style>
        /* Force text on all dashboard buttons to be bright white */
        .stButton > button {
            color: #FFFFFF !important;
            background-color: #1b263b !important; /* Matches your card container background */
            border: 1px solid #415a77 !important; /* Clean, professional border */
        }
        
        /* Keep text white during hover, active click, or focus states */
        .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
            color: #FFFFFF !important;
            background-color: #2c3e50 !important; /* Slight background shift for click feedback */
            border-color: #778da9 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📊 Cyber Security Dashboard")
    st.write("Welcome to the main workspace. Click on any tool below to begin your security assessment.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("🔐 Password Strength Checker")
            st.write("Analyze character rules and receive instant improvement tips.")
            if st.button("Open Password Tool", use_container_width=True):
                st.session_state.page = "password"
                st.rerun()
                
        st.write("") # Spacing
        
        with st.container(border=True):
            st.subheader("🎣 Phishing Message Parser")
            st.write("Scan emails or suspicious text alerts for spam trigger words.")
            if st.button("Open Phishing Tool", use_container_width=True):
                st.session_state.page = "phishing"
                st.rerun()
                
    with col2:
        with st.container(border=True):
            st.subheader("🌐 URL Integrity Checker")
            st.write("Check if a link uses proper encryption protocols before visiting.")
            if st.button("Open URL Tool", use_container_width=True):
                st.session_state.page = "url"
                st.rerun()
                
        st.write("") # Spacing
        
        with st.container(border=True):
            st.subheader("🤖 Cyber Security AI Assistant")
            st.write("Ask questions regarding security guidelines and best practices.")
            if st.button("Open AI Assistant", use_container_width=True):
                st.session_state.page = "ai"
                st.rerun()

# --- PASSWORD CHECKER PAGE ---
elif st.session_state.page == "password":
    # 🚨 FIX PLACED HERE: This forces the input label and button text to be bright white at all times
    st.markdown("""
        <style>
        /* Force input field labels to be bright white */
        .stWidgetFormLabel, label, [data-testid="stWidgetLabel"] p {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        
        /* Force the Back button text to be bright white */
        .stButton > button {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        
        /* Keep button text white during hover or focus states */
        .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
            color: #FFFFFF !important;
            background-color: #2c3e50 !important;
            border-color: #778da9 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🔐 Password Strength Checker")
    st.write("Test your password structure. For safety reasons, do not type your real everyday password.")
    st.markdown("---")
    
    user_password = st.text_input("Enter a test password:", type="password")
    
    if user_password:
        # Strength Criteria Check
        has_length = len(user_password) >= 8
        has_upper = re.search("[A-Z]", user_password) is not None
        has_number = re.search("[0-9]", user_password) is not None
        has_special = re.search("[@#$%^&*!_?]", user_password) is not None
        
        # Calculate Score
        score = sum([has_length, has_upper, has_number, has_special])
        
        st.subheader("Analysis Results:")
        if score <= 1:
            st.error("❌ Weak Password")
        elif score <= 3:
            st.warning("⚠️ Medium Password")
        else:
            st.success("✅ Strong Password")
            
        # Display Checklist Feedback
        st.write(f"**Score:** {score} out of 4 criteria met")
        st.checkbox("At least 8 characters long", value=has_length, disabled=True)
        st.checkbox("Contains an uppercase letter (A-Z)", value=has_upper, disabled=True)
        st.checkbox("Contains a number (0-9)", value=has_number, disabled=True)
        st.checkbox("Contains a special character (@, #, $, %, etc.)", value=has_special, disabled=True)
        
        # Simple Suggestions
        st.markdown("#### 💡 Tips to improve:")
        if not has_length: st.write("- Make your password longer (at least 8 to 12 characters).")
        if not has_upper: st.write("- Add at least one capital letter.")
        if not has_number: st.write("- Include one or more numbers.")
        if not has_special: st.write("- Use special symbols like ! or @ to make it harder to guess.")
        if score == 4: st.write("- Perfect! Your password structure looks great.")
        
    st.markdown("---")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
        
# --- PHISHING DETECTOR PAGE ---
elif st.session_state.page == "phishing":
    # 🚨 INTEGRATED VISIBILITY FIX
    st.markdown("""
        <style>
        /* Force text area input label to be bright white */
        .stWidgetFormLabel, label, [data-testid="stWidgetLabel"] p {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        /* Force pasted text inside the text area to be bright white */
        .stTextArea textarea {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Force page action and back buttons to be permanently white */
        .stButton > button {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Keep button text white during hover or focus states */
        .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
            color: #FFFFFF !important;
            background-color: #2c3e50 !important;
            border-color: #778da9 !important;
        }
        /* Ensure headers match crisp white theme */
        h1, h2, h3, h4 {
            color: #FFFFFF !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎣 Phishing Message Detector")
    st.write("Paste an email or text message below to scan for common social engineering terms.")
    st.markdown("---")
    
    message_input = st.text_area("Paste message content here:", height=150)
    
    # List of common phishing terms
    phishing_keywords = ["urgent", "verify", "suspended", "bank", "otp", "login", "password", "winner", "click here", "lottery"]
    
    if message_input:
        found_words = [word for word in phishing_keywords if word in message_input.lower()]
        word_count = len(found_words)
        
        st.subheader("Risk Assessment:")
        if word_count >= 2:
            st.error("🚨 High Risk: This message contains multiple suspicious terms often used in scams.")
        elif word_count == 1:
            st.warning("⚠️ Caution: One suspicious term detected. Double-check the sender's identity.")
        else:
            st.success("✅ Low Risk: No obvious phishing trigger words found in the text.")
            
        if found_words:
            st.markdown(f"**Highlighted Suspicious Words:** {', '.join(found_words)}")
            
        st.markdown("""
        **💡 Standard Safety Rules:**
        * Never click links inside unexpected text messages or emails.
        * Official organizations will not ask for your password or OTP over a text message.
        """)
        
    st.markdown("---")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

# --- URL SAFETY CHECKER PAGE ---
elif st.session_state.page == "url":
    # 🚨 INTEGRATED VISIBILITY FIX
    st.markdown("""
        <style>
        /* Force URL input text label to be bright white */
        .stWidgetFormLabel, label, [data-testid="stWidgetLabel"] p {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        /* Force the typed web address link content to be readable white */
        .stTextInput input {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Force the Back button text to be bright white */
        .stButton > button {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Keep button text white during hover or focus states */
        .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
            color: #FFFFFF !important;
            background-color: #2c3e50 !important;
            border-color: #778da9 !important;
        }
        /* Ensure headers match crisp white theme */
        h1, h2, h3 {
            color: #FFFFFF !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🌐 URL Safety Checker")
    st.write("Analyze structural and protocol elements of a website link.")
    st.markdown("---")
    
    url_input = st.text_input("Enter URL to check (e.g., https://example.com):")
    
    if url_input:
        st.subheader("Result:")
        
        # Check for secure protocol prefix
        if url_input.lower().startswith("https://"):
            st.success("🔒 Secure Protocol (HTTPS): The communication channel to this website is encrypted.")
            st.info("Note: Even if a site uses HTTPS, always make sure the domain name is spelled correctly (e.g., look out for fake sites like 'g00gle.com').")
        elif url_input.lower().startswith("http://"):
            st.error("⚠️ Unencrypted Protocol (HTTP): This website does not use modern encryption. Avoid entering sensitive data like login details or card numbers.")
        else:
            st.warning("❓ Incomplete Link: Please include the full prefix protocol (http:// or https://) to check its safety accurately.")
            
    st.markdown("---")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()


# --- AI ASSISTANT PAGE ---
# --- AI ASSISTANT PAGE ---
elif st.session_state.page == "ai":
    # 🚨 INTEGRATED VISIBILITY FIX
    st.markdown("""
        <style>
        /* Force user query input text label to be bright white */
        .stWidgetFormLabel, label, [data-testid="stWidgetLabel"] p {
            color: #FFFFFF !important;
            font-weight: 500 !important;
        }
        /* Force interactive typed question inputs to display bright white text */
        .stTextInput input {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Force quick FAQ buttons and system back buttons to stay white */
        .stButton > button {
            color: #FFFFFF !important;
            background-color: #1b263b !important;
            border: 1px solid #415a77 !important;
        }
        /* Keep button text white during hover or focus states */
        .stButton > button:hover, .stButton > button:active, .stButton > button:focus {
            color: #FFFFFF !important;
            background-color: #2c3e50 !important;
            border-color: #778da9 !important;
        }
        /* Ensure headers match crisp white theme */
        h1, h2, h3 {
            color: #FFFFFF !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🤖 Cyber Security AI Assistant")
    st.write("Ask basic questions regarding online safety practices or cybersecurity definitions.")
    st.markdown("---")
    
    # Quick Option Buttons to simulate a chat guide instantly
    st.write("**Frequently Asked Questions:**")
    col_q1, col_q2, col_q3 = st.columns(3)
    
    chosen_prompt = ""
    with col_q1:
        if st.button("How do I stay safe online?", use_container_width=True):
            chosen_prompt = "How do I stay safe online?"
    with col_q2:
        if st.button("What is Two-Factor Authentication?", use_container_width=True):
            chosen_prompt = "What is Two-Factor Authentication?"
    with col_q3:
        if st.button("How can I spot a phishing email?", use_container_width=True):
            chosen_prompt = "How can I spot a phishing email?"
            
    # Regular Custom Input Box
    user_query = st.text_input("Or type your own question here:", value=chosen_prompt)
    
    if user_query:
        st.markdown(f"**Question:** {user_query}")
        st.markdown("**Answer:**")
        
        query_lower = user_query.lower()
        if "safe" in query_lower or "online" in query_lower:
            st.write("1. Use separate, unique passwords for every online account.\n"
                     "2. Turn on Two-Factor Authentication (2FA) wherever available.\n"
                     "3. Keep your mobile phone apps and computer operating systems updated.\n"
                     "4. Avoid logging into personal banking profiles on free public Wi-Fi networks.")
        elif "authentication" in query_lower or "2fa" in query_lower:
            st.write("Two-Factor Authentication (2FA) adds an extra step of safety. "
                     "Instead of just your password, it requires a second piece of evidence—such as a temporary text message code sent to your phone or an authenticator app token. This stops attackers from entering even if they steal your password.")
        elif "phishing" in query_lower or "email" in query_lower:
            st.write("1. Check the sender's full email address closely to spot misspellings.\n"
                     "2. Look out for generic greetings like 'Dear Customer' instead of your real name.\n"
                     "3. Watch out for urgent or threatening language demanding quick actions.\n"
                     "4. Hover over links to check where they point before clicking.")
        else:
            st.write("Always maintain healthy habits online. Keep your passwords strong, don't share verification codes with anyone, and don't download unverified software attachments from random emails.")
            
    st.markdown("---")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()


# 4. FIXED PROFESSIONAL ACADEMIC FOOTER
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #a1a1aa; font-size: 14px; padding: 10px;">
        <strong>Project Presentation Portal</strong><br>
        Developed by: <b>Komalpreet Kaur</b> | Student, BCA Cyber Security
    </div>
    """, 
    unsafe_allow_html=True
)
