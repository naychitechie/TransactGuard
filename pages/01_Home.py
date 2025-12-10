"""Home page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar
import os

st.set_page_config(page_title="Home - TransactGuard", layout="wide")
apply_dark_theme()

# Hero section: embed image as a data URI so it reliably loads, then overlay text
import base64
from pathlib import Path

img_path = Path(__file__).resolve().parents[1] / "assets" / "images" / "b5.png"
data_uri = ""
if img_path.exists():
        with open(img_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                data_uri = f"data:image/png;base64,{encoded}"
else:
        # fallback to the relative path if file isn't found for some reason
        data_uri = "assets/images/background-image.png"

st.markdown(f"""
<div class="hero-section-wrapper">
    <img class="hero-bg" src="{data_uri}" alt="Hero background" />
    <div class="hero-text-overlay">
        <h1 class="hero-title">Real-Time Fraud Detection Powered by AI</h1>
        <p style="font-size: 16px; color: var(--text-secondary); max-width: 800px; margin: 24px auto;">
            Detect high-risk transactions instantly with advanced machine-learning models engineered for accuracy, speed, and trust.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

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
