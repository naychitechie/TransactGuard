"""Home page - TransactGuard AI Fraud Detection"""
import streamlit as st
from src.styles import apply_base_theme, render_sidebar

# Page config
st.set_page_config(
    page_title="Home - TransactGuard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Apply base theme
apply_base_theme()

# Render sidebar
render_sidebar()

# Page content
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="font-size: 3rem; margin-bottom: 1rem;">🛡️ TransactGuard</h1>
    <h2 style="font-size: 1.5rem; color: #9ca3af; margin-bottom: 2rem;">AI-Powered Fraud Detection System</h2>
    <p style="font-size: 1.1rem; max-width: 600px; margin: 0 auto; color: #d1d5db;">
        Protect your transactions with cutting-edge machine learning technology. 
        Real-time fraud detection powered by advanced AI algorithms.
    </p>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3 style="text-align: center;">🧠 AI Powered</h3>
        <p style="text-align: center; color: #9ca3af;">
            Advanced machine learning models trained on millions of transactions
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 style="text-align: center;">⚡ Real-time</h3>
        <p style="text-align: center; color: #9ca3af;">
            Instant fraud detection with millisecond response times
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3 style="text-align: center;">🔐 Secure</h3>
        <p style="text-align: center; color: #9ca3af;">
            Bank-level encryption and data protection standards
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA section
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    if st.button("🔍 Start Analyzing Transactions", use_container_width=True, key="home_cta"):
        st.switch_page("pages/02_Predict.py")

st.markdown("<br>", unsafe_allow_html=True)

# Stats section
st.markdown("""
<div style="text-align: center; padding: 2rem; background: rgba(10, 14, 39, 0.5); border-radius: 12px; border: 1px solid rgba(13, 110, 253, 0.15);">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem;">
        <div>
            <h2 style="font-size: 2.5rem; margin: 0; background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">99.8%</h2>
            <p style="color: #9ca3af; margin: 0.5rem 0 0 0;">Accuracy</p>
        </div>
        <div>
            <h2 style="font-size: 2.5rem; margin: 0; background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">&lt;10ms</h2>
            <p style="color: #9ca3af; margin: 0.5rem 0 0 0;">Response Time</p>
        </div>
        <div>
            <h2 style="font-size: 2.5rem; margin: 0; background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">24/7</h2>
            <p style="color: #9ca3af; margin: 0.5rem 0 0 0;">Protection</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)