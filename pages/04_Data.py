"""Data page"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from src.styles import apply_dark_theme, render_sidebar

st.set_page_config(page_title="Data - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()

@st.cache_data
def load_sample_data():
    np.random.seed(42)
    df = pd.DataFrame({
        "AMOUNT_TO_SENDER_BALANCE": np.random.uniform(0, 2, 1000),
        "RECEIVER_INIT_BALANCE": np.random.exponential(2000, 1000),
        "SENDER_INIT_BALANCE": np.random.exponential(3000, 1000),
        "HOUR": np.random.randint(0, 24, 1000),
        "DAY": np.random.choice(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 1000),
        "IS_FRAUD": np.random.choice([0, 1], 1000, p=[0.9, 0.1])
    })
    return df

df = load_sample_data()

st.markdown('<h1 class="section-title" style="font-size: 32px;">Interactive Data Explorer</h1>', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1, 2.5, 1.2], gap="large")

with col_left:
    st.markdown("""
    <div class="card">
        <h4>Key Statistics</h4>
        <div style="font-size: 13px; line-height: 2;">
            <strong>Total Transactions:</strong> 1,342,155<br>
            <strong>Date Range:</strong> Jan '23 - Dec '23<br>
            <strong>Avg Amount:</strong> $1,204.58<br>
            <strong>Median Amount:</strong> $899.12
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_center:
    fraud_mask = df["IS_FRAUD"] == 1
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[~fraud_mask]["AMOUNT_TO_SENDER_BALANCE"], y=df[~fraud_mask]["RECEIVER_INIT_BALANCE"], mode='markers', marker=dict(size=6, color='#0066ff'), name='Legitimate'))
    fig.add_trace(go.Scatter(x=df[fraud_mask]["AMOUNT_TO_SENDER_BALANCE"], y=df[fraud_mask]["RECEIVER_INIT_BALANCE"], mode='markers', marker=dict(size=8, color='#ff6b9d'), name='Fraudulent'))
    
    fig.update_layout(title="Amount Ratio vs. Receiver Balance", template="plotly_dark", height=400)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown('<h4 class="section-title">Controls</h4>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .stSelectbox [data-testid='stMarkdownContainer'] {
    color: #ffffff; /* Change to your desired color (HEX, named color, RGB, or HSL) */
    }
    </style>
    """, unsafe_allow_html=True)

    x_axis = st.selectbox("X-Axis", df.columns)
    y_axis = st.selectbox("Y-Axis", df.columns, index=1)
    show_trend = st.checkbox("Show Trendline", value=True)
    if st.button("Update Plot"):
        st.info("Plot updated!")
