"""TransactGuard - Fraud Transaction Prediction Tool"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(
    page_title="TransactGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_dark_theme()

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

st.switch_page("pages/01_Home.py")

render_sidebar()
