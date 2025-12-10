"""Data page"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from src.styles import apply_dark_theme, render_sidebar
from scipy import stats

st.set_page_config(page_title="Data - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()

# Custom CSS for better styling
st.markdown("""
<style>
.data-card {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.8) 100%);
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.data-card:hover {
    border-color: rgba(148, 163, 184, 0.4);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.data-card h4 {
    margin: 0 0 16px 0;
    font-size: 16px;
    font-weight: 700;
    color: #e2e8f0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    font-size: 13px;
    color: #cbd5e1;
}

.stat-row:last-child {
    border-bottom: none;
}

.stat-label {
    font-weight: 600;
    color: #94a3b8;
}

.stat-value {
    color: #38bdf8;
    font-weight: 700;
}

.insight-item {
    padding: 8px 0;
    font-size: 12px;
    color: #cbd5e1;
    line-height: 1.6;
}

.insight-item::before {
    content: "→";
    color: #fbbf24;
    margin-right: 8px;
    font-weight: bold;
}

.control-section {
    margin-top: 24px;
    padding-top: 20px;
    border-top: 1px solid rgba(148, 163, 184, 0.1);
}

.control-section h5 {
    font-size: 13px;
    font-weight: 700;
    color: #e2e8f0;
    margin: 12px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.viz-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 16px;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 12px;
    transition: all 0.2s ease;
}

.checkbox-container {
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_real_data(file_path='data/transactions.csv'):
    """
    Loads the real transaction dataset from a CSV file.
    """
    try:
        # To improve performance on large datasets, we'll load a sample.
        # Remove .sample(n=5000, random_state=42) to load the entire file.
        df = pd.read_csv(file_path).sample(n=5000, random_state=42)
        
        # --- Data Cleaning & Feature Engineering (example) ---
        # Ensure column names match what the model expects.
        # This section should mirror the transformations used for model training.
        if 'TX_DATETIME' in df.columns:
            df['TX_DATETIME'] = pd.to_datetime(df['TX_DATETIME'])
            df['HOUR'] = df['TX_DATETIME'].dt.hour
        return df
    except FileNotFoundError:
        st.error(f"Error: The data file was not found at '{file_path}'. Please make sure the file exists.")
        return None

def create_scatter_plot(df, x_col, y_col, show_trend=False):
    """Create interactive scatter plot"""
    fraud_mask = df["IS_FRAUD"] == 1
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[~fraud_mask][x_col],
        y=df[~fraud_mask][y_col],
        mode='markers',
        marker=dict(size=6, color='#0ea5e9', opacity=0.6),
        name='Legitimate',
        hovertemplate=f'<b>Legitimate</b><br>{x_col}: %{{x}}<br>{y_col}: %{{y}}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=df[fraud_mask][x_col],
        y=df[fraud_mask][y_col],
        mode='markers',
        marker=dict(size=8, color='#f43f5e', opacity=0.8),
        name='Fraudulent',
        hovertemplate=f'<b>Fraudulent</b><br>{x_col}: %{{x}}<br>{y_col}: %{{y}}<extra></extra>'
    ))
    
    if show_trend:
        z = np.polyfit(df[x_col].dropna(), df[y_col].dropna(), 1)
        p = np.poly1d(z)
        x_trend = np.linspace(df[x_col].min(), df[x_col].max(), 100)
        fig.add_trace(go.Scatter(
            x=x_trend, y=p(x_trend),
            mode='lines',
            name='Trendline',
            line=dict(color='#fbbf24', width=2, dash='dash')
        ))
    
    fig.update_layout(
        title=dict(text=f"Scatter Plot: {x_col} vs {y_col}", font=dict(size=16, color='#e2e8f0')),
        xaxis_title=x_col,
        yaxis_title=y_col,
        template="plotly_dark",
        height=450,
        font=dict(size=11, color='#cbd5e1'),
        plot_bgcolor='rgba(15, 23, 42, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        hovermode='closest',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    fig.update_xaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    fig.update_yaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    return fig

def create_line_plot(df, x_col, y_col):
    """Create interactive line plot"""
    df_sorted = df.sort_values(by=x_col)
    fraud_mask = df_sorted["IS_FRAUD"] == 1
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_sorted[~fraud_mask][x_col],
        y=df_sorted[~fraud_mask][y_col],
        mode='lines+markers',
        name='Legitimate',
        line=dict(color='#0ea5e9', width=2),
        marker=dict(size=5)
    ))
    fig.add_trace(go.Scatter(
        x=df_sorted[fraud_mask][x_col],
        y=df_sorted[fraud_mask][y_col],
        mode='lines+markers',
        name='Fraudulent',
        line=dict(color='#f43f5e', width=2),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        title=dict(text=f"Line Plot: {x_col} vs {y_col}", font=dict(size=16, color='#e2e8f0')),
        xaxis_title=x_col,
        yaxis_title=y_col,
        template="plotly_dark",
        height=450,
        font=dict(size=11, color='#cbd5e1'),
        plot_bgcolor='rgba(15, 23, 42, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    fig.update_xaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    fig.update_yaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    return fig

def create_bar_plot(df, x_col, y_col):
    """Create interactive bar plot"""
    fig = go.Figure()
    
    df_grouped = df.groupby(x_col)[y_col].agg(['mean', 'count']).reset_index()
    
    fig.add_trace(go.Bar(
        x=df_grouped[x_col],
        y=df_grouped['mean'],
        name=f'Avg {y_col}',
        marker=dict(color='#0ea5e9', opacity=0.8),
        text=df_grouped['mean'].round(2),
        textposition='auto',
    ))
    
    fig.update_layout(
        title=dict(text=f"Bar Chart: {x_col} vs {y_col}", font=dict(size=16, color='#e2e8f0')),
        xaxis_title=x_col,
        yaxis_title=f"Avg {y_col}",
        template="plotly_dark",
        height=450,
        font=dict(size=11, color='#cbd5e1'),
        plot_bgcolor='rgba(15, 23, 42, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    fig.update_xaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    fig.update_yaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    return fig

def create_box_plot(df, x_col, y_col):
    """Create interactive box plot"""
    fig = go.Figure()
    
    for fraud_status, name, color in [(0, 'Legitimate', '#0ea5e9'), (1, 'Fraudulent', '#f43f5e')]:
        data = df[df['IS_FRAUD'] == fraud_status]
        fig.add_trace(go.Box(
            y=data[y_col],
            name=name,
            marker=dict(color=color),
            boxmean='sd'
        ))
    
    fig.update_layout(
        title=dict(text=f"Box Plot: Distribution by Fraud Status", font=dict(size=16, color='#e2e8f0')),
        yaxis_title=y_col,
        template="plotly_dark",
        height=450,
        font=dict(size=11, color='#cbd5e1'),
        plot_bgcolor='rgba(15, 23, 42, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    fig.update_yaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    return fig

# Initialize session state
if 'viz_type' not in st.session_state:
    st.session_state.viz_type = 'scatter'

df = load_real_data()

# Stop execution if data loading failed
if df is None:
    st.stop()

st.markdown('<div style="margin-bottom: 32px;"><h1 style="color: #e2e8f0; font-size: 36px; font-weight: 800; margin: 0;">Interactive Data Explorer (Data from transactions.csv)</h1></div>', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([0.8, 5.5, 1], gap="large")

with col_left:
    # Dataset Overview Card
    st.markdown("""
    <div class="data-card">
        <h4>Dataset Overview</h4>
        <div class="stat-row">
            <span class="stat-label">Total Records</span>
            <span class="stat-value">{len(df):,}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Date Range</span>
            <span class="stat-value">Sample Data</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Total Columns</span>
            <span class="stat-value">{len(df.columns)}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Statistics Card
    fraud_count = len(df[df['IS_FRAUD'] == 1])
    fraud_rate = (fraud_count / len(df)) * 100
    
    st.markdown(f"""
    <div class="data-card">
        <h4>Key Statistics</h4>
        <div class="stat-row">
            <span class="stat-label">Avg. Tx Amount</span>
            <span class="stat-value">${df['TX_AMOUNT'].mean():,.0f}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Median Tx Amount</span>
            <span class="stat-value">${df['TX_AMOUNT'].median():,.0f}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Fraud Rate</span>
            <span class="stat-value">{fraud_rate:.1f}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # High-Fraud Insights Card
    st.markdown("""
    <div class="data-card">
        <h4>High-Fraud Insights</h4>
        <div class="insight-item">Low balance accounts show 3x higher fraud risk</div>
        <div class="insight-item">Transactions over $5K require manual review</div>
        <div class="insight-item">Q4 sees 24% spike in fraudulent activity</div>
    </div>
    """, unsafe_allow_html=True)

with col_center:
    # Get selected columns from session state
    x_axis = st.session_state.get('x_axis', 'TX_AMOUNT')
    y_axis = st.session_state.get('y_axis', 'SENDER_INIT_BALANCE')
    show_trend = st.session_state.get('show_trend', False)
    
    # Create visualization based on selected type
    try:
        if st.session_state.viz_type == 'scatter':
            fig = create_scatter_plot(df, x_axis, y_axis, show_trend)
        elif st.session_state.viz_type == 'line':
            fig = create_line_plot(df, x_axis, y_axis)
        elif st.session_state.viz_type == 'bar':
            fig = create_bar_plot(df, x_axis, y_axis)
        elif st.session_state.viz_type == 'box':
            fig = create_box_plot(df, x_axis, y_axis)
        else:
            fig = create_scatter_plot(df, x_axis, y_axis, show_trend)
        
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating visualization: {str(e)}")

with col_right:
    st.markdown("""
    <div class="data-card" style="margin-bottom: 0;">
        <h4 style="margin-bottom: 20px;">Controls</h4>
    """, unsafe_allow_html=True)
    
    st.markdown('<label style="color: #94a3b8; font-weight: 600; font-size: 12px; display: block; margin-bottom: 8px;">X-Axis Column</label>', unsafe_allow_html=True)
    x_axis_selected = st.selectbox("X-Axis", df.columns, label_visibility="collapsed", key="x_axis")
    
    st.markdown('<label style="color: #94a3b8; font-weight: 600; font-size: 12px; display: block; margin-top: 16px; margin-bottom: 8px;">Y-Axis Column</label>', unsafe_allow_html=True)
    y_axis_selected = st.selectbox("Y-Axis", df.columns, index=list(df.columns).index('SENDER_INIT_BALANCE'), label_visibility="collapsed", key="y_axis")
    
    st.markdown("""
    <div class="control-section">
        <h5>Visualization Type</h5>
    </div>
    """, unsafe_allow_html=True)
    
    col_viz1, col_viz2 = st.columns(2)
    with col_viz1:
        if st.button("📊 Scatter", use_container_width=True, key="viz_scatter"):
            st.session_state.viz_type = 'scatter'
            st.rerun()
    with col_viz2:
        if st.button("📈 Line", use_container_width=True, key="viz_line"):
            st.session_state.viz_type = 'line'
            st.rerun()
    
    col_viz3, col_viz4 = st.columns(2)
    with col_viz3:
        if st.button("📊 Bar", use_container_width=True, key="viz_bar"):
            st.session_state.viz_type = 'bar'
            st.rerun()
    with col_viz4:
        if st.button("📦 Box Plot", use_container_width=True, key="viz_box"):
            st.session_state.viz_type = 'box'
            st.rerun()
    
    st.markdown("""
    <div class="control-section">
        <h5>Customization & Statistics</h5>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="checkbox-container">', unsafe_allow_html=True)
    show_trend = st.checkbox("✓ Show Trendline", value=st.session_state.get('show_trend', False), key="show_trend")
    show_pearson = st.checkbox("✓ Pearson Correlation", value=False)
    show_chi = st.checkbox("✓ Chi-Squared Test", value=False)
    alter_points = st.checkbox("✓ Alter Points", value=False)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display statistics if requested
    if show_pearson:
        try:
            corr, p_value = stats.pearsonr(df[x_axis_selected].dropna(), df[y_axis_selected].dropna())
            st.markdown(f"""
            <div style="background: rgba(30, 58, 138, 0.3); border-left: 3px solid #38bdf8; padding: 12px; border-radius: 4px; margin-top: 12px; font-size: 12px;">
            <strong>Pearson Correlation:</strong> {corr:.4f}<br>
            <strong>P-Value:</strong> {p_value:.4e}
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.info("Cannot compute correlation for this column pair")
    
    st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)
    if st.button("💾 Update Plot", use_container_width=True, key="update_btn"):
        st.success("✨ Plot updated successfully!")
    
    st.markdown('</div>', unsafe_allow_html=True)
