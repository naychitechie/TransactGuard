"""Predict page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar
from src.prediction_service import get_fraud_prediction

st.set_page_config(page_title="Predict - TransactGuard", layout="wide", initial_sidebar_state="collapsed")
apply_dark_theme()
render_sidebar()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="form-container"><h1 style="color: var(--text-primary); font-size: 28px; font-weight: 700;">Predict Transaction Fraud</h1></div>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Transaction Amount</label>', unsafe_allow_html=True)
        transaction_amount = st.number_input("Transaction Amount", min_value=0.0, label_visibility="collapsed", key="amt")
    
    with col_b:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Sender Initial Balance</label>', unsafe_allow_html=True)
        sender_balance = st.number_input("Sender Initial Balance", min_value=0.0, label_visibility="collapsed", key="sb")
    
    col_c, col_d = st.columns(2)
    with col_c:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Sender Behavior ID</label>', unsafe_allow_html=True)
        sender_behavior_id = st.selectbox("Sender Behavior ID", ["BehaviorID-12345", "BehaviorID-67890", "BehaviorID-54321", "BehaviorID-09876"], label_visibility="collapsed")
    
    with col_d:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Receiver Initial Balance</label>', unsafe_allow_html=True)
        receiver_balance = st.number_input("Receiver Initial Balance", min_value=0.0, label_visibility="collapsed", key="rb")
    
    col_e, col_f = st.columns(2)
    with col_e:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Day of the Week</label>', unsafe_allow_html=True)
        day_of_week = st.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], label_visibility="collapsed")
    
    with col_f:
        st.markdown('<label style="color: var(--text-primary); font-weight: 600;">Hour</label>', unsafe_allow_html=True)
        hour = st.number_input("Hour", min_value=0, max_value=23, label_visibility="collapsed", key="hr")
    
    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
    
    if st.button("🔮 Predict", use_container_width=True):
        result = get_fraud_prediction(transaction_amount, sender_balance, receiver_balance, sender_behavior_id, day_of_week, int(hour))
        st.session_state.prediction_result = result
        st.switch_page("pages/03_Results.py")
