"""Predict page - TransactGuard AI Fraud Detection"""
import streamlit as st
from src.styles import apply_base_theme, apply_predict_theme, render_header, render_section_header, render_field_label, render_sidebar, start_form_wrapper, end_form_wrapper

# Page config
st.set_page_config(
    page_title="Predict - TransactGuard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Apply themes
apply_base_theme()
apply_predict_theme()

# Render sidebar
render_sidebar()

# Render banner header at top
render_header()

# Start form wrapper
start_form_wrapper()

# Transaction Details Section
render_section_header("💳", "Transaction Details")

col1, col2 = st.columns(2)
with col1:
    render_field_label("Transaction Amount")
    tx_amount = st.number_input(
        "tx_amt", 
        min_value=0.0, 
        value=100.0, 
        step=10.0, 
        label_visibility="collapsed", 
        key="tx_amt", 
        format="%.2f"
    )

with col2:
    render_field_label("Sender Behavior ID")
    sender_behavior_id = st.selectbox(
        "behavior", 
        options=[1, 2, 3, 4, 5], 
        index=2, 
        label_visibility="collapsed", 
        key="behavior_id"
    )

# Account Balance Section
render_section_header("💰", "Account Balances")

col3, col4 = st.columns(2)
with col3:
    render_field_label("Sender Initial Balance")
    sender_balance = st.number_input(
        "sender_bal", 
        min_value=0.0, 
        value=5000.0, 
        step=100.0, 
        label_visibility="collapsed", 
        key="sender_bal", 
        format="%.2f"
    )

with col4:
    render_field_label("Receiver Initial Balance")
    receiver_balance = st.number_input(
        "receiver_bal", 
        min_value=0.0, 
        value=3000.0, 
        step=100.0, 
        label_visibility="collapsed", 
        key="receiver_bal", 
        format="%.2f"
    )

# Calculate the ratio - LIVE UPDATE
amount_to_balance_ratio = tx_amount / sender_balance if sender_balance > 0 else 0

# Display the ratio card with animated transfer icon
st.markdown(f"""
<div class="ratio-display">
    <div class="ratio-label">
        <span class="transfer-icon"></span>
        Amount to Sender Balance Ratio
    </div>
    <div class="ratio-value">{amount_to_balance_ratio:.4f}</div>
</div>
""", unsafe_allow_html=True)

# Warning if amount exceeds balance
if tx_amount > sender_balance:
    st.markdown('<div class="warning-box">⚠️ Transaction amount exceeds sender balance</div>', unsafe_allow_html=True)

# Transaction Timing Section
render_section_header("🕐", "Transaction Timing")

col5, col6 = st.columns(2)
with col5:
    render_field_label("Day of Week")
    day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_display = st.selectbox(
        "day", 
        options=day_options, 
        index=0, 
        label_visibility="collapsed", 
        key="day_week"
    )
    day_of_week = day_options.index(day_display)

with col6:
    render_field_label("Hour of Transaction")
    hour = st.slider(
        "hour", 
        min_value=0, 
        max_value=23, 
        value=14, 
        label_visibility="collapsed", 
        key="hour_slider"
    )
    
    if 5 <= hour < 12:
        period, color = "Morning", "#fbbf24"
    elif 12 <= hour < 17:
        period, color = "Afternoon", "#f59e0b"
    elif 17 <= hour < 21:
        period, color = "Evening", "#a855f7"
    else:
        period, color = "Night", "#3b82f6"
    
    st.markdown(f'<div class="time-badge" style="color: {color};">{hour:02d}:00 • {period}</div>', unsafe_allow_html=True)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Button
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    predict_disabled = tx_amount > sender_balance
    if st.button("🔍 Analyze Transaction", key="predict_btn", disabled=predict_disabled, use_container_width=True):
        
        st.session_state.prediction_input = {
            "amount_to_balance_ratio": amount_to_balance_ratio,
            "sender_behavior_id": sender_behavior_id,
            "tx_amount": tx_amount,
            "sender_balance": sender_balance,
            "receiver_balance": receiver_balance,
            "day_of_week": day_of_week,
            "hour": hour
        }
        
        # Mock prediction result
        result = {
            "is_fraud": amount_to_balance_ratio > 0.5 if sender_balance > 0 else True,
            "confidence": 0.87,
            "risk_score": amount_to_balance_ratio if sender_balance > 0 else 1.0
        }
        
        st.session_state.prediction_result = result
        st.switch_page("pages/03_Results.py")

st.markdown('<div class="security-note">🔒 Your data is encrypted and secure</div>', unsafe_allow_html=True)

# End form wrapper
end_form_wrapper()