"""Results page - TransactGuard AI Fraud Detection"""
import streamlit as st
from src.styles import apply_base_theme, render_sidebar

# Page config
st.set_page_config(
    page_title="Results - TransactGuard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Apply base theme
apply_base_theme()

# Render sidebar
render_sidebar()

# Check if we have prediction results
if "prediction_result" not in st.session_state or st.session_state.prediction_result is None:
    st.warning("⚠️ No prediction results found. Please make a prediction first.")
    if st.button("Go to Prediction Page"):
        st.switch_page("pages/02_Predict.py")
    st.stop()

# Get the results
result = st.session_state.prediction_result
input_data = st.session_state.get("prediction_input", {})

# Page header
st.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊 Analysis Results</h1>
    <p style="color: #9ca3af;">Transaction fraud detection report</p>
</div>
""", unsafe_allow_html=True)

# Main result card
if result.get("is_fraud", False):
    status_color = "#ef4444"
    status_bg = "rgba(239, 68, 68, 0.1)"
    status_border = "rgba(239, 68, 68, 0.3)"
    status_text = "⚠️ FRAUD DETECTED"
    status_message = "This transaction shows high risk indicators"
else:
    status_color = "#10b981"
    status_bg = "rgba(16, 185, 129, 0.1)"
    status_border = "rgba(16, 185, 129, 0.3)"
    status_text = "✅ LEGITIMATE"
    status_message = "This transaction appears to be safe"

st.markdown(f"""
<div style="background: {status_bg}; border: 2px solid {status_border}; border-radius: 16px; padding: 2rem; text-align: center; margin-bottom: 2rem;">
    <h2 style="color: {status_color}; font-size: 2rem; margin: 0;">{status_text}</h2>
    <p style="color: {status_color}; margin-top: 0.5rem; font-size: 1.1rem;">{status_message}</p>
</div>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Confidence Score</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0; color: {status_color};">{result.get('confidence', 0)*100:.1f}%</h3>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Risk Score</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0; color: {status_color};">{result.get('risk_score', 0):.3f}</h3>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card" style="text-align: center;">
        <p style="color: #9ca3af; font-size: 0.9rem; margin: 0;">Amount</p>
        <h3 style="font-size: 2rem; margin: 0.5rem 0;">${input_data.get('tx_amount', 0):,.2f}</h3>
    </div>
    """, unsafe_allow_html=True)

# Transaction details
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📋 Transaction Details")

st.markdown(f"""
<div class="card">
    <p><strong>Transaction Amount:</strong> ${input_data.get('tx_amount', 0):,.2f}</p>
    <p><strong>Sender Balance:</strong> ${input_data.get('sender_balance', 0):,.2f}</p>
    <p><strong>Receiver Balance:</strong> ${input_data.get('receiver_balance', 0):,.2f}</p>
    <p><strong>Amount to Balance Ratio:</strong> {input_data.get('amount_to_balance_ratio', 0):.4f}</p>
    <p><strong>Sender Behavior ID:</strong> {input_data.get('sender_behavior_id', 'N/A')}</p>
    <p><strong>Day of Week:</strong> {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][input_data.get('day_of_week', 0)]}</p>
    <p><strong>Hour:</strong> {input_data.get('hour', 0):02d}:00</p>
</div>
""", unsafe_allow_html=True)

# Action buttons
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Analyze Another Transaction", use_container_width=True):
        st.switch_page("pages/02_Predict.py")

with col2:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/01_Home.py")