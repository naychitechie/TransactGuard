"""About page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="About - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()

st.markdown('<h1 class="section-title" style="font-size: 36px;">About Us</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Who We Are</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
We are TransactGuard, a dynamic team of AI students from the Southern Alberta Institute of Technology (SAIT).<br><br>
United by a passion for financial security and machine learning, we developed TransactGuard—a cutting-edge solution designed to detect fraudulent transactions. Our mission is to leverage advanced algorithms to build a safer digital economy.
</div>
""", unsafe_allow_html=True)

team = [
    ("Dany", "Project Coordinator and UI Designer"),
    ("Nay", "Technical Lead and Developer"),
    ("Ohm", "Deployment Lead"),
    ("Rithiek", "ML Integration Lead"),
    ("Angel", "Testing and Documentation Lead")
]

col_left, col_right = st.columns([1.2, 1], gap="large")
with col_left:
    for name, role in team:
        st.markdown(f'<div class="card"><strong>{name}</strong> - {role}</div>', unsafe_allow_html=True)

with col_right:
    st.image("assets/images/team_photo.jpg", width=360)

st.markdown('<h2 class="section-title">Strengths</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
<ul style="margin: 0 0 0 18px; padding: 0; color: var(--text-primary);">
  <li>10+ years combined experience</li>
  <li>Technical diversity</li>
  <li>Data analysis expertise</li>
  <li>Fresh ideas</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Our Work Philosophy</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">We value collaboration, learning, and mutual support.</div>', unsafe_allow_html=True)
