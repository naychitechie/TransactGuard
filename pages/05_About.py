"""About page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="About - TransactGuard", layout="wide", initial_sidebar_state="collapsed")
apply_dark_theme()
render_sidebar()

st.markdown('<h1 class="section-title" style="font-size: 36px;">About Us</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
st.markdown("")
st.markdown('<div class="card">We are Freshbuilders, AI students from SAIT. We developed TransactGuard to detect fraud in transactions using machine learning.</div>', unsafe_allow_html=True)

team = [
    ("Dany", "Project Coordinator and UI Designer"),
    ("Nay", "Technical Lead and Developer"),
    ("Ohm", "Deployment Lead"),
    ("Rithiek", "ML Integration Lead"),
    ("Angel", "Testing and Documentation Lead")
]

for name, role in team:
    st.markdown(f'<div class="card"><strong>{name}</strong> - {role}</div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Strengths</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">10+ years combined experience • Technical diversity • Data analysis expertise • Fresh ideas</div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Challenges & Solutions</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">Limited ML experience • Diverse backgrounds • Mentorship & pair programming support</div>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Our Work Philosophy</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">We value collaboration, learning, and mutual support.</div>', unsafe_allow_html=True)
