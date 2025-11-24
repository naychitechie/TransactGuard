"""Home page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="Home - TransactGuard", layout="wide", initial_sidebar_state="collapsed")
apply_dark_theme()
render_sidebar()

st.image("assets/images/logo.png", use_container_width=True)  # or width=1200

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Fraud Transaction Prediction</h1>
    <p style="font-size: 16px; color: var(--text-secondary); max-width: 600px; margin: 24px auto;">
        Predict fraudulent transactions with precision and confidence. Our advanced algorithms analyze transaction data in real-time.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("🚀 Get Started"):
        st.switch_page("pages/02_Predict.py")

st.markdown('<h2 class="section-title">Real-Life Fraud Transactions</h2>', unsafe_allow_html=True)

fraud_types = [
    ("Unauthorized Credit Card Use", "A credit card was used without owner consent."),
    ("Phishing Scams", "User tricked into providing sensitive information."),
    ("Account Takeover", "Attacker gained control of user account."),
    ("Identity Theft", "Personal information stolen and used for fraud.")
]

cols = st.columns(4)
emojis = ["💳", "🎣", "🔓", "🙋"]
for idx, (title, desc) in enumerate(fraud_types):
    with cols[idx]:
        st.markdown(f'<div class="card" style="text-align: center;"><div style="font-size: 48px;">{emojis[idx]}</div><h3 style="font-size: 16px; font-weight: 600;">{title}</h3><p style="font-size: 12px; color: var(--text-secondary);">{desc}</p></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Our Process</h2>', unsafe_allow_html=True)

steps = [
    ("📥", "Data Collection", "Gather transaction data from various sources."),
    ("🔍", "Analysis and Prediction", "Analyze patterns and predict fraud."),
    ("📊", "Insights", "Provide insights on fraud prevention.")
]

cols = st.columns(3)
for icon, title, desc in steps:
    with cols[0] if icon == "📥" else cols[1] if icon == "🔍" else cols[2]:
        st.markdown(f'<div class="card"><div style="font-size: 32px;">{icon}</div><h3 style="font-size: 18px;">{title}</h3><p style="color: var(--text-secondary);">{desc}</p></div>', unsafe_allow_html=True)
