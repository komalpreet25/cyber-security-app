import streamlit as st
import re
def set_bg(color1, color2):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(to right, {color1}, {color2}) !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# 🤖 Sidebar AI
set_bg("#481e72", "#2a9298")   # Blue gradient
st.sidebar.title("🤖 AI Assistant") 
user_input = st.sidebar.text_input("Ask me anything")

if user_input:
    if "password" in user_input.lower():
        st.sidebar.write("Use strong password with symbols 🔐")
    elif "phishing" in user_input.lower():
        st.sidebar.write("Avoid clicking unknown links ⚠️")
    else:
        st.sidebar.write("Stay safe online 💻")

# Page control
if "page" not in st.session_state:
    st.session_state.page = "home"

# 🏠 HOME PAGE
if st.session_state.page == "home":
    set_bg("#56721e", "#98942a")   # Blue gradient
    st.title("🚀 AI Powered Cyber Security Assistant")
    st.markdown("### 🔐 Stay Safe | 🧠 Smart AI | 🌐 Secure Web")

    if st.button("Enter App"):
        st.session_state.page = "dashboard"

# 📊 DASHBOARD
elif st.session_state.page == "dashboard":
    set_bg("#bac35c", "#E1DB37")   # Dark blue-black
    st.title("📊 Dashboard")
    st.markdown("""
### 📌 About This Project
This is an AI-powered Cyber Security Assistant that helps users:
- Check password strength 🔐
- Detect phishing messages 🕵️
- Analyze URL safety 🌐
- Get cyber security tips using AI 🤖

Built using Python and Streamlit.
""")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    if col1.button("🔐 Password Checker 🔵"):
        st.session_state.page = "password"

    if col2.button("🕵️ Phishing Detector 🔴"):
        st.session_state.page = "phishing"

    if col3.button("🌐 URL Checker 🟢"):
        st.session_state.page = "url"

    if col4.button("🤖 AI Assistant 🟣"):
        st.session_state.page = "ai"

# 🔐 PASSWORD PAGE
elif st.session_state.page == "password":
    set_bg("#11998e", "#734b6d")   # Purple
    st.title("🔐 Password Checker")
    st.markdown("### 📌 Check how strong your password is")
    st.markdown("""
👉 Enter your password below to analyze its strength and security level.
""")
    password = st.text_input("Enter password", type="password")

    def check_password(password):
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search("[A-Z]", password):
            score += 1
        if re.search("[0-9]", password):
            score += 1
        if re.search("[@#$%^&*]", password):
            score += 1
        return score

    if password:
        score = check_password(password)

        if score <= 1:
            st.error("Weak Password ❌")
        elif score <= 3:
            st.warning("Medium Password ⚠️")
        else:
            st.success("Strong Password ✅")

        st.write(f"Security Score: {score}/4")
        st.markdown("💡 Tip: Use uppercase, numbers & symbols")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"

# 🕵️ PHISHING PAGE
elif st.session_state.page == "phishing":
    set_bg("#ff416c", "#ff4b2b")   # Red alert style
    st.title("🕵️ Phishing Detector")
    st.markdown("### 📌 Detect suspicious messages")
    st.markdown("""
👉 Paste a message/email below to check if it's a phishing attempt.
""")

    text = st.text_area("Paste message/email")

    phishing_words = ["urgent", "click", "verify", "password", "bank", "otp"]

    if text:
        score = 0
        for word in phishing_words:
            if word in text.lower():
                score += 1

        if score >= 2:
            st.error("⚠️ Phishing Detected!")
        else:
            st.success("✅ Safe Message")

        st.write(f"Risk Score: {score}")
        st.markdown("💡 Tip: Never click unknown links")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"

# 🌐 URL CHECKER
elif st.session_state.page == "url":
    set_bg("#11998e", "#38ef7d")   # Green safe vibe
    st.title("🌐 URL Safety Checker")
    st.markdown("### 📌 Check if a website is safe")
    
    url = st.text_input("Enter URL")

    if url:
        if "https" in url:
            st.success("Safe Website ✅")
        else:
            st.error("⚠️ Suspicious URL")
            st.markdown("### 📌 Check if a website is safe")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"

# 🤖 AI page

elif st.session_state.page == "ai":
    set_bg("#8e2de2", "#4a00e0")   # AI purple-blue
    st.title("🤖 AI Cyber Assistant")
    st.markdown("### 📌 Ask anything about cyber security")
    st.markdown("""
👉 Get tips about passwords, phishing, and online safety.
""")
    msg = st.text_input("Ask your question")

    if msg:
        if "password" in msg.lower():
            st.write("""
🔐 A strong password should be at least 8-12 characters long and include a mix of uppercase letters, lowercase letters, numbers, and special symbols like @, #, or $.

👉 Avoid using common words like your name, birthdate, or simple patterns like 123456.

👉 Try using a passphrase, for example: "MyDog@2024Secure" which is easy to remember but hard to guess.

👉 Never reuse the same password across multiple websites.

👉 Enable two-factor authentication (2FA) wherever possible for extra security.

👉 Use a password manager to safely store and generate strong passwords.

👉 Always update your passwords regularly to stay protected.

💡 Tip: The more random and longer your password is, the safer it will be.
""")

        elif "phishing" in msg.lower():
            st.write("""
⚠️ Phishing is a cyber attack where attackers try to trick you into giving personal information like passwords or bank details.

👉 Always check the sender's email address carefully.

👉 Avoid clicking on suspicious links or attachments.

👉 Look for spelling mistakes or urgent messages like "Click now!"

👉 Never share OTP or passwords with anyone.

👉 Always verify the website URL before entering sensitive information.

💡 Tip: If something feels urgent or too good to be true, it's likely a scam.
""")

        else:
            st.write("""
💻 Stay safe online by following good cyber security practices.

👉 Use strong passwords for all accounts.

👉 Avoid public WiFi for sensitive work.

👉 Keep your system updated.

👉 Install antivirus software.

👉 Always be cautious while downloading files.

💡 Tip: Awareness is the best protection against cyber threats.
""")

    if st.button("⬅ Back"):
        st.session_state.page = "dashboard"
