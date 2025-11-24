"""Results page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="Results - TransactGuard", layout="wide", initial_sidebar_state="collapsed")
apply_dark_theme()
render_sidebar()

if not st.session_state.get("prediction_result"):
    st.warning("No prediction result found.")
    if st.button("Go to Predict"):
        st.switch_page("pages/02_Predict.py")
    st.stop()

result = st.session_state.prediction_result

st.markdown('<h1 style="color: var(--text-primary); font-size: 36px;">Prediction Result</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    color = "#ffe0ed" if result["is_fraudulent"] else "#e0f2fe"
    st.markdown(f'<div class="card" style="background-color: {color};"><div style="color: #666; font-size: 12px;">Prediction Result</div><div style="color: #000; font-size: 28px; font-weight: 700;">{result["prediction"]}</div></div>', unsafe_allow_html=True)

with col2:
    color = "#ffe0ed" if result["risk_level"] == "High" else "#fff3cd" if result["risk_level"] == "Medium" else "#e0f2fe"
    st.markdown(f'<div class="card" style="background-color: {color};"><div style="color: #666; font-size: 12px;">Risk Level</div><div style="color: #000; font-size: 28px; font-weight: 700;">{result["risk_level"]}</div></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Transaction Details</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="card"><div style="color: var(--text-secondary); font-size: 12px;">Transaction Amount</div><div style="color: var(--text-primary); font-size: 20px; font-weight: 700;">${result["transaction_amount"]:,.2f}</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card"><div style="color: var(--text-secondary); font-size: 12px;">Sender Initial Balance</div><div style="color: var(--text-primary); font-size: 20px; font-weight: 700;">${result["sender_balance"]:,.2f}</div></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Prediction Key Drivers</h2>', unsafe_allow_html=True)

for factor_text, is_factor in result["fraud_factors"]:
    st.markdown(f'<div style="display: flex; margin-bottom: 12px;"><input type="checkbox" {"checked" if is_factor else ""} disabled style="margin-right: 12px;"><span style="color: var(--text-primary);">{factor_text}</span></div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Model Insight</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="card"><div style="color: var(--text-secondary);">Probability Score</div><div style="color: var(--text-primary); font-size: 24px; font-weight: 700;">{result["probability"]:.2f}</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card"><div style="color: var(--text-secondary);">vs Similar Transactions</div><div style="color: var(--text-primary);">{result["comparison_insight"]}</div></div>', unsafe_allow_html=True)
