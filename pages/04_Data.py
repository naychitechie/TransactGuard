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
# render_sidebar()

# Custom CSS for better styling
st.markdown("""
<style>
.data-card {
    background: linear-gradient(135deg, rgba(13, 110, 253, 0.12) 0%, rgba(138, 43, 226, 0.12) 100%);
    border: 1px solid rgba(13, 110, 253, 0.3);
    border-radius: 20px;
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
    font-size: 12px; 
    display: block; 
    margin-bottom: 8px
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
    background: linear-gradient(135deg, rgba(13, 110, 253, 0.12) 0%, rgba(138, 43, 226, 0.12) 100%);
    border: 1px solid rgba(13, 110, 253, 0.3);
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px; /* Set a fixed height for vertical centering */
    margin-top: 10px;
    margin-bottom: 10px; /* Add space below the separator */
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

#  .ratio-display {
#         background: linear-gradient(135deg, rgba(13, 110, 253, 0.12) 0%, rgba(138, 43, 226, 0.12) 100%);
#         border: 1px solid rgba(13, 110, 253, 0.3);
#         border-radius: 20px;
#         padding: 2.5rem;
#         margin: 2.5rem 0;
#         text-align: center;
#         position: relative;
#         overflow: hidden;
#     }
                       
.control-section h4 {
    margin: 0; /* Remove margin to allow flex centering */
    font-size: 16px;
    font-weight: 700;
    color: #e2e8f0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}
.control-section h5 {
    font-size: 13px;
    font-weight: 700;
    color: #e2e8f0;
    margin: 0; /* Remove margin to allow flex centering */
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}
      
.viz-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 16px;
}

.checkbox-container {
    margin: 8px 0;
    font-style: normal;
}

/* Apply stat-label styles to selectbox labels in the right column */
[data-testid="stVerticalBlock"] .stSelectbox label {
    font-weight: 600 !important;
    color: #94a3b8 !important;
    font-size: 12px !important;
}

/* Custom styles for visualization buttons */
.viz-button-container .stButton button {
    background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 8px 26px rgba(13, 110, 253, 0.32) !important;
        text-transform: uppercase !important;
        letter-spacing: 3.5px !important;
        transition: all 0.3s ease !important;
        min-height: 52px !important;
        animation: buttonGlow 3s ease-in-out infinite;
        line-height: 1.1 !important;
}

/* Hover state for the small visualization buttons */
.viz-button-container .stButton button:hover {
    background-color: rgba(51, 65, 85, 0.9) !important;
    border-color: #64748b !important;
}
                    
/* Custom styles for the small visualization buttons */
# .viz-button-container .stButton > button {
#     background: rgba(30, 41, 59, 0.8) !important;
#     border: 1px solid #475569 !important;
#     color: #cbd5e1 !important;
#     font-size: 0.9rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.5px !important;
#     text-transform: none !important;
#     padding: 0.75rem 0.5rem !important;
#     min-height: 40px !important;
#     animation: none !important;
#     box-shadow: none !important;
# }

/* Local Selectbox Styling to override global defaults */
.data-page-selectbox .stSelectbox > div > div {
    background-color: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(148, 163, 184, 0.2) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}
.data-page-selectbox .stSelectbox div[data-baseweb="select"] > div {
    background-color: transparent !important;
    color: #e2e8f0 !important;
}
            
.data-page-selectbox .stSelectbox div[data-baseweb="select"] * {
    background-color: transparent !important;
}
                  

/* Specific style for a primary action button on the Data page */
.data-primary-button .stButton > button {
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 1rem 2.2rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 8px 26px rgba(13, 110, 253, 0.32) !important;
        text-transform: uppercase !important;
        letter-spacing: 3.5px !important;
        transition: all 0.3s ease !important;
        min-height: 52px !important;
        animation: buttonGlow 3s ease-in-out infinite;
        line-height: 1.1 !important;
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
        hovertemplate=f'<b>Legitimate</b><br><br><b>{x_col}:</b> %{{x}}<br><b>{y_col}:</b> %{{y}}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=df[fraud_mask][x_col],
        y=df[fraud_mask][y_col],
        mode='markers',
        marker=dict(size=8, color='#f43f5e', opacity=0.8),
        name='Fraudulent',
        hovertemplate=f'<b>Fraudulent</b><br><br><b>{x_col}:</b> %{{x}}<br><b>{y_col}:</b> %{{y}}<extra></extra>'
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
        margin=dict(l=50, r=50, t=50, b=50),
        hoverlabel=dict(
            bgcolor="#1e293b",
            font_color="#cbd5e1" # Set global font color for the tooltip
        )
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
        hovertemplate=f'<b>Legitimate</b><br><br><b>{x_col}:</b> %{{x}}<br><b>{y_col}:</b> %{{y}}<extra></extra>',
        line=dict(color='#0ea5e9', width=2),
        marker=dict(size=5)
    ))
    fig.add_trace(go.Scatter(
        x=df_sorted[fraud_mask][x_col],
        y=df_sorted[fraud_mask][y_col],
        mode='lines+markers',
        name='Fraudulent',
        hovertemplate=f'<b>Fraudulent</b><br><br><b>{x_col}:</b> %{{x}}<br><b>{y_col}:</b> %{{y}}<extra></extra>',
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
        margin=dict(l=50, r=50, t=50, b=50),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="#1e293b",
            font_color="#cbd5e1" # Set global font color for the tooltip
        )
    )
    fig.update_xaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    fig.update_yaxes(gridcolor='rgba(148, 163, 184, 0.1)', showgrid=True)
    return fig

def create_bar_plot(df, x_col, y_col):
    """Create interactive bar plot"""
    # If x_col is numeric, bin it for a meaningful bar chart
    if pd.api.types.is_numeric_dtype(df[x_col]) and df[x_col].nunique() > 20:
        # Create 10 bins for the numeric data
        df_copy = df.copy()
        df_copy[f'{x_col}_bin'] = pd.cut(df_copy[x_col], bins=10)
        
        # Group by the new bins
        df_grouped = df_copy.groupby(f'{x_col}_bin')[y_col].mean().reset_index()
        x_data = df_grouped[f'{x_col}_bin'].astype(str) # Use bin labels for x-axis
        y_data = df_grouped[y_col]
        x_title = f'{x_col} (Binned)'
    else:
        # For categorical data, group by unique values
        df_grouped = df.groupby(x_col)[y_col].mean().reset_index()
        x_data = df_grouped[x_col]
        y_data = df_grouped[y_col]
        x_title = x_col

    fig = px.bar(x=x_data, y=y_data, labels={'x': x_title, 'y': f'Average {y_col}'}, text_auto='.2s')
    fig.update_traces(marker_color='#0ea5e9', marker_line_width=0)

    fig.update_layout(
        title=dict(text=f"Bar Chart: {x_title} vs Average {y_col}", font=dict(size=16, color='#e2e8f0')),
        xaxis_title=x_title,
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
            hovertemplate=f'<b>{name}</b><br><b>{y_col}:</b> %{{y}}<extra></extra>',
            marker=dict(color=color),
            boxmean='sd'
        ))
    
    fig.update_layout(
        title=dict(text=f"Box Plot: Distribution by Fraud Status", font=dict(size=16, color='#e2e8f0')),
        yaxis_title=y_col,
        xaxis_title="Status",
        template="plotly_dark",
        height=450,
        font=dict(size=11, color='#cbd5e1'),
        plot_bgcolor='rgba(15, 23, 42, 0.5)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=50, r=50, t=50, b=50),
        hoverlabel=dict(
            bgcolor="#1e293b",
            font_color="#cbd5e1" # Set global font color for the tooltip
        )
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

st.markdown('<div style="margin-bottom: 32px;"><h1 style="color: #e2e8f0; font-size: 36px; font-weight: 800; margin: 0; text-align: center;">Interactive Data Explorer</h1></div>', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1, 3, 1.5], gap="small")

with col_left:
    # Dataset Overview Card
    st.markdown(f"""
    <div class="data-card">
        <h4>Dataset Overview</h4>
        <div class="stat-row">
            <span class="stat-label">Total Records</span>
            <span class="stat-value">{len(df):,}</span>
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
    # st.markdown("""
    # <div class="data-card">
    #     <h4>High-Fraud Insights</h4>
    #     <div class="insight-item">Low balance accounts show 3x higher fraud risk</div>
    #     <div class="insight-item">Transactions over $5K require manual review</div>
    #     <div class="insight-item">Q4 sees 24% spike in fraudulent activity</div>
    # </div>
    # """, unsafe_allow_html=True)

with col_center:
    # This block will be executed after the controls in the right column are rendered
    pass

with col_right:
    st.markdown("""
    <div class="control-section"">
        <h4>Plot Controls</h4>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="data-page-selectbox">', unsafe_allow_html=True)
    
    # Use native labels for a cleaner look and automatic updates
    x_axis = st.selectbox(
        "X-Axis", 
        df.columns, 
        key="x_axis", 
        index=list(df.columns).index('TX_AMOUNT'),
    )
    y_axis = st.selectbox(
        "Y-Axis", 
        df.columns, 
        key="y_axis", 
        index=list(df.columns).index('SENDER_INIT_BALANCE'),
    )
    st.markdown('</div>', unsafe_allow_html=True)
            
    st.markdown('<div class="control-section"><h4>Visualization Type</h4></div>', unsafe_allow_html=True)
    st.markdown('<div class="viz-button-container">', unsafe_allow_html=True)
    col_viz1, col_viz2 = st.columns(2)
    with col_viz1:
        if st.button("Scatter", use_container_width=True, key="viz_scatter"):
            st.session_state.viz_type = 'scatter'
            st.rerun()
    with col_viz2:
        if st.button("Line", use_container_width=True, key="viz_line"):
            st.session_state.viz_type = 'line'
            st.rerun()
    
    col_viz3, col_viz4 = st.columns(2)
    with col_viz3:
        if st.button("Bar", use_container_width=True, key="viz_bar"):
            st.session_state.viz_type = 'bar'
            st.rerun()
    with col_viz4:
        if st.button("Box", use_container_width=True, key="viz_box"):
            st.session_state.viz_type = 'box'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # st.markdown('<div class="control-section"><h4>Customization & Statistics</h4></div>', unsafe_allow_html=True)
    # st.markdown('<div class="checkbox-container">', unsafe_allow_html=True)
    # show_trend = st.checkbox("Show Trendline", value=st.session_state.get('show_trend', False), key="show_trend")
    # show_pearson = st.checkbox("Pearson Correlation", value=False)
    # st.markdown('</div>', unsafe_allow_html=True)
    
    # Display statistics if requested
    # if show_pearson:
    #     # Add a small top margin to separate from the checkbox
    #     st.markdown('<div style="margin-top: 12px;"></div>', unsafe_allow_html=True)
    #     try:
    #         corr, p_value = stats.pearsonr(df[x_axis].dropna(), df[y_axis].dropna())
    #         st.markdown(f"""
    #         <div style="background: rgba(30, 58, 138, 0.3); border-left: 3px solid #38bdf8; padding: 12px; border-radius: 4px; margin-top: 12px; font-size: 12px;">
    #         <strong>Pearson Correlation:</strong> {corr:.4f}<br>
    #         <strong>P-Value:</strong> {p_value:.4e}
    #         </div>
    #         """, unsafe_allow_html=True)
    #     except (ValueError, TypeError):
    #         st.info("Cannot compute correlation for this column pair.")
    
    # st.markdown('</div>', unsafe_allow_html=True)

# Now, render the plot in the center column using the values from the controls
with col_center:
    x_axis = st.session_state.get('x_axis', 'TX_AMOUNT')
    y_axis = st.session_state.get('y_axis', 'SENDER_INIT_BALANCE')
    show_trend = st.session_state.get('show_trend', False)

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
        
        #  To remove the toolbar/unnecessary buttons for a cleaner look
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    except Exception as e:
        st.error(f"Error creating visualization: {str(e)}")
