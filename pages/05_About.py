"""About page - TransactGuard AI Fraud Detection"""
import streamlit as st
from src.styles import apply_base_theme, render_sidebar

# Page config
st.set_page_config(
    page_title="About - TransactGuard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Apply base theme
apply_base_theme()

# Render sidebar
render_sidebar()

# Page header
st.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">ℹ️ About TransactGuard</h1>
    <p style="color: #9ca3af;">AI-Powered Fraud Detection System</p>
</div>
""", unsafe_allow_html=True)

# About section
st.markdown("### 🛡️ What is TransactGuard?")
st.markdown("""
<div class="card">
    <p>
        TransactGuard is an advanced AI-powered fraud detection system designed to protect 
        financial transactions in real-time. Using state-of-the-art machine learning algorithms, 
        our system analyzes transaction patterns, behavior anomalies, and risk indicators to 
        identify potentially fraudulent activities with high accuracy.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Features
st.markdown("### ✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>🧠 Machine Learning Powered</h4>
        <p style="color: #9ca3af; font-size: 0.9rem;">
            Advanced ML models trained on millions of transaction records to detect 
            fraud patterns with exceptional accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4>⚡ Real-time Analysis</h4>
        <p style="color: #9ca3af; font-size: 0.9rem;">
            Instant fraud detection with response times under 10 milliseconds, 
            ensuring seamless transaction processing.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🔐 Enterprise Security</h4>
        <p style="color: #9ca3af; font-size: 0.9rem;">
            Bank-level encryption and security protocols to protect your 
            sensitive transaction data.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4>📊 Detailed Analytics</h4>
        <p style="color: #9ca3af; font-size: 0.9rem;">
            Comprehensive reporting and analytics to understand fraud patterns 
            and improve security measures.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Technology stack
st.markdown("### 🔧 Technology Stack")
st.markdown("""
<div class="card">
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
        <div style="padding: 0.5rem 1rem; background: rgba(13, 110, 253, 0.1); border: 1px solid rgba(13, 110, 253, 0.3); border-radius: 20px; font-size: 0.9rem;">
            Python
        </div>
        <div style="padding: 0.5rem 1rem; background: rgba(13, 110, 253, 0.1); border: 1px solid rgba(13, 110, 253, 0.3); border-radius: 20px; font-size: 0.9rem;">
            Streamlit
        </div>
        <div style="padding: 0.5rem 1rem; background: rgba(13, 110, 253, 0.1); border: 1px solid rgba(13, 110, 253, 0.3); border-radius: 20px; font-size: 0.9rem;">
            Scikit-learn
        </div>
        <div style="padding: 0.5rem 1rem; background: rgba(13, 110, 253, 0.1); border: 1px solid rgba(13, 110, 253, 0.3); border-radius: 20px; font-size: 0.9rem;">
            Pandas
        </div>
        <div style="padding: 0.5rem 1rem; background: rgba(13, 110, 253, 0.1); border: 1px solid rgba(13, 110, 253, 0.3); border-radius: 20px; font-size: 0.9rem;">
            TensorFlow
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Team
st.markdown("### 👥 Development Team")
st.markdown("""
<div class="card" style="text-align: center;">
    <h4>Freshbuilders - SAIT</h4>
    <p style="color: #9ca3af; font-size: 0.9rem;">
        Built with ❤️ by the Freshbuilders team at Southern Alberta Institute of Technology
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    if st.button("🔍 Try TransactGuard Now", use_container_width=True):
        st.switch_page("pages/02_Predict.py")