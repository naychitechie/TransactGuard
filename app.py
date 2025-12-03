"""TransactGuard - Fraud Transaction Prediction Tool"""
import streamlit as st
from src.styles import apply_base_theme, render_sidebar

st.set_page_config(
    page_title="TransactGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply base theme
apply_base_theme()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# Navigate to home page
st.switch_page("pages/01_Home.py")

# Render sidebar
render_sidebar()