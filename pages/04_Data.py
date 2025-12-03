"""Data page - TransactGuard AI Fraud Detection"""
import streamlit as st
from src.styles import apply_base_theme, render_sidebar

# Page config
st.set_page_config(
    page_title="Data - TransactGuard", 
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
    <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">📋 Transaction Data</h1>
    <p style="color: #9ca3af;">View and analyze transaction history</p>
</div>
""", unsafe_allow_html=True)

# Sample data section
st.markdown("### 📊 Sample Transaction Dataset")

st.markdown("""
<div class="card">
    <p>This page would display your transaction data, analytics, and historical information.</p>
    <p style="color: #9ca3af; font-size: 0.9rem;">Features coming soon:</p>
    <ul style="color: #9ca3af; font-size: 0.9rem;">
        <li>Transaction history table</li>
        <li>Data filtering and search</li>
        <li>Export functionality</li>
        <li>Statistical summaries</li>
        <li>Visualization charts</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Placeholder metrics
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Total Transactions</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0;">1,234</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Fraud Detected</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0; color: #ef4444;">87</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Legitimate</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0; color: #10b981;">1,147</h3>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Fraud Rate</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0;">7.05%</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    if st.button("🔍 Analyze New Transaction", use_container_width=True):
        st.switch_page("pages/02_Predict.py")