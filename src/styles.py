"""Styling helpers for TransactGuard Streamlit app.

Provides centralized styling functions that pages can import.
All CSS and visual components are defined here for consistency.
"""
import streamlit as st


def apply_base_theme():
    """Apply base dark theme used across all pages."""
    base_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    :root {
        --dark-bg: #192B39;
        --card-bg: #1a1f2e;
        --text-primary: #ffffff;
        --text-secondary: #ffffff;
        --sidebar-bg: var(--dark-bg);
        --accent-blue: #0066ff;
        --accent-pink: #ff6b9d;
        --border-color: #2a3142;
    }

    

    /* Hide Streamlit's built-in navigation */
    [data-testid="stSidebar"] nav,
    [data-testid="stSidebar"] [role="navigation"],
    [data-testid="stSidebar"] ul,
    [data-testid="stSidebar"] .css-1d391kg {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Hide anchor links on headers */
    .stMarkdown a, 
    h1 a, h2 a, h3 a,
    [data-testid="StyledLinkIconContainer"] {
        display: none !important;
    }

    /* Header background */
    header, [data-testid="stHeader"] {
        background-color: var(--dark-bg) !important;
        color: var(--text-primary) !important;
    }

    /* Main app background */
    [data-testid="stAppViewContainer"] { 
        background-color: var(--dark-bg) !important; 
    }
    
    main, body, .appview-container, .reportview-container { 
        background-color: var(--dark-bg) !important; 
    }
    
    body { 
        min-height: 100vh; 
    }

    /* Sidebar */
    [data-testid="stSidebar"] { 
        background-color: var(--sidebar-bg) !important;
        min-width: 300px !important;
        width: 300px !important;
        flex-grow: 0 !important;
    }
    
    [data-testid="stSidebar"] > div {
        width: 100% !important;
        padding-top: 2rem !important;
    }
    
    /* Sidebar Title */
    [data-testid="stSidebar"] h3 {
        font-size: 1.5rem !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
    }
    
    /* Sidebar Buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        margin: 0.8rem 0 !important;
        padding: 1.2rem 1.5rem !important;
        font-size: 1.1rem !important;
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.2) 0%, rgba(138, 43, 226, 0.1) 100%) !important;
        border: 1px solid rgba(13, 110, 253, 0.4) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.4) 0%, rgba(138, 43, 226, 0.25) 100%) !important;
        border-color: rgba(13, 110, 253, 0.7) !important;
        box-shadow: 0 0 20px rgba(13, 110, 253, 0.3) !important;
        transform: translateX(8px) !important;
    }

    /* Card styling */
    .card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        color: var(--text-secondary) !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #0A1117 !important;
        color: #ffffff !important;
        border: none !important;
        padding: 10px 16px !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
    }

    div.stButton > button:hover {
        background-color: #254057 !important;
    }

    /* Input fields */
    div.stTextInput > div > div > input,
    div.stNumberInput > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1.5px solid rgba(13, 110, 253, 0.3) !important;
        border-radius: 12px !important;
        padding: 18px 22px !important;
        font-size: 1.15rem !important;
        transition: all 0.3s ease !important;
        min-height: 56px !important;
    }
    
    div.stTextInput > div > div > input:focus,
    div.stNumberInput > div > input:focus {
        border-color: rgba(13, 110, 253, 0.7) !important;
        box-shadow: 0 0 20px rgba(13, 110, 253, 0.4) !important;
    }
    
    /* Selectbox styling */
    div.stSelectbox > div > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1.5px solid rgba(13, 110, 253, 0.3) !important;
        border-radius: 12px !important;
        padding: 18px 22px !important;
        font-size: 1.15rem !important;
        min-height: 56px !important;
    }
    
    /* Dropdown arrow icon */
    div.stSelectbox svg {
        color: rgba(13, 110, 253, 0.7) !important;
        width: 30px !important;
        height: 30px !important;
        stroke-width: 2px !important;
    }
    
    /* Slider styling */
    div.stSlider > div > div > div {
        background: linear-gradient(to right, rgba(13, 110, 253, 0.4), rgba(138, 43, 226, 0.4)) !important;
    }
    </style>
    """
    st.markdown(base_css, unsafe_allow_html=True)


def apply_predict_theme():
    """Apply the animated theme specifically for the Predict page."""
    predict_css = """
    <style>
    /* Animated Background */
    .stApp {
        background: 
            radial-gradient(ellipse at 0% 0%, rgba(13, 110, 253, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 100% 0%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 100% 100%, rgba(13, 110, 253, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 0% 100%, rgba(138, 43, 226, 0.15) 0%, transparent 50%),
            linear-gradient(180deg, #080b1a 0%, #0f1629 50%, #080b1a 100%);
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
    }
    
    /* Animated gradient overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(13, 110, 253, 0.1) 0%, transparent 25%),
            radial-gradient(circle at 80% 50%, rgba(138, 43, 226, 0.1) 0%, transparent 25%);
        animation: bgPulse 8s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes bgPulse {
        0%, 100% { opacity: 0.5; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
    }
    
    /* Floating particles */
    .stApp::after {
        content: '';
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, rgba(13, 110, 253, 0.3), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(138, 43, 226, 0.3), transparent),
            radial-gradient(2px 2px at 50px 160px, rgba(13, 110, 253, 0.3), transparent),
            radial-gradient(2px 2px at 90px 40px, rgba(138, 43, 226, 0.3), transparent),
            radial-gradient(2px 2px at 130px 80px, rgba(13, 110, 253, 0.3), transparent),
            radial-gradient(2px 2px at 160px 120px, rgba(138, 43, 226, 0.3), transparent);
        background-size: 400px 200px;
        animation: particleFloat 20s linear infinite;
        pointer-events: none;
        z-index: 0;
        opacity: 0.6;
    }
    
    @keyframes particleFloat {
        0% { transform: translateY(0); }
        100% { transform: translateY(-200px); }
    }
    
    .stApp > .main {
        position: relative;
        z-index: 1;
    }
    
    /* Container for Predict Page */
    .block-container {
        padding: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
        background: transparent !important;
        margin: 0 !important;
        position: relative;
        border-radius: 0 !important;
    }
    
    /* Banner Header */
    .banner-header {
        width: 100%;
        background: rgba(15, 23, 42, 0.98);
        backdrop-filter: blur(30px);
        border-bottom: 3px solid rgba(13, 110, 253, 0.4);
        padding: 2.5rem 2rem 1.5rem 2rem;
        flex-shrink: 0;
        box-shadow: 0 0 60px rgba(13, 110, 253, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: bannerGlow 3s ease-in-out infinite;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.2rem;
        justify-content: center;
    }
    
    @keyframes bannerGlow {
        0%, 100% { 
            border-color: rgba(13, 110, 253, 0.5);
            box-shadow: 0 0 60px rgba(13, 110, 253, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        50% { 
            border-color: rgba(138, 43, 226, 0.6);
            box-shadow: 0 0 80px rgba(138, 43, 226, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15);
        }
    }
    
    /* Form Wrapper - Rectangle */
    .form-wrapper {
        width: calc(100% - 3rem);
        max-width: 1400px;
        background: rgba(10, 14, 35, 0.92);
        backdrop-filter: blur(30px);
        border: 2.5px solid rgba(13, 110, 253, 0.5);
        border-radius: 28px;
        padding: 4rem 5rem;
        box-shadow: 
            0 0 40px rgba(13, 110, 253, 0.4),
            0 0 80px rgba(138, 43, 226, 0.25),
            0 25px 80px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        animation: formGlow 3s ease-in-out infinite;
    }
    
    @keyframes formGlow {
        0%, 100% { 
            border-color: rgba(13, 110, 253, 0.5);
            box-shadow: 
                0 0 40px rgba(13, 110, 253, 0.4),
                0 0 80px rgba(138, 43, 226, 0.25),
                0 25px 80px rgba(0, 0, 0, 0.6),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        50% { 
            border-color: rgba(138, 43, 226, 0.6);
            box-shadow: 
                0 0 50px rgba(138, 43, 226, 0.4),
                0 0 100px rgba(13, 110, 253, 0.35),
                0 30px 100px rgba(0, 0, 0, 0.7),
                inset 0 1px 0 rgba(255, 255, 255, 0.15);
        }
    }
    
    /* Header Card - Banner Style */
    .header-card {
        background: transparent;
        backdrop-filter: none;
        border: none;
        border-radius: 0;
        padding: 0;
        margin: 0;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
    }
    
    /* Animated Logo */
    .logo-container {
        position: relative;
        width: 70px;
        height: 70px;
        margin: 0;
        flex-shrink: 0;
    }
    
    .logo-outer-ring {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 2px solid rgba(13, 110, 253, 0.3);
        border-radius: 50%;
        animation: ringRotate 8s linear infinite;
    }
    
    .logo-outer-ring::before {
        content: '';
        position: absolute;
        top: -2px;
        left: 50%;
        width: 8px;
        height: 8px;
        background: #0d6efd;
        border-radius: 50%;
        transform: translateX(-50%);
        box-shadow: 0 0 10px #0d6efd;
    }
    
    @keyframes ringRotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .logo-inner-ring {
        position: absolute;
        top: 8px;
        left: 8px;
        right: 8px;
        bottom: 8px;
        border: 2px dashed rgba(138, 43, 226, 0.4);
        border-radius: 50%;
        animation: ringRotate 6s linear infinite reverse;
    }
    
    .logo-core {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 45px;
        height: 45px;
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 50%, #00d4ff 100%);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        box-shadow: 
            0 0 20px rgba(13, 110, 253, 0.5),
            0 0 40px rgba(138, 43, 226, 0.3);
        animation: corePulse 3s ease-in-out infinite;
    }
    
    @keyframes corePulse {
        0%, 100% { 
            transform: translate(-50%, -50%) scale(1);
            box-shadow: 
                0 0 20px rgba(13, 110, 253, 0.5),
                0 0 40px rgba(138, 43, 226, 0.3);
        }
        50% { 
            transform: translate(-50%, -50%) scale(1.05);
            box-shadow: 
                0 0 30px rgba(13, 110, 253, 0.7),
                0 0 50px rgba(138, 43, 226, 0.5);
        }
    }
    
    /* Brand Name */
    .brand-name {
        font-size: 3.8rem;
        font-weight: 900;
        letter-spacing: 3px;
        margin-bottom: 0;
        position: relative;
        display: inline-block;
    }
    
    .brand-name .text-gradient {
        background: linear-gradient(135deg, #fff 0%, #0d6efd 50%, #8a2be2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 200% auto;
        animation: textShine 4s linear infinite;
    }
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    .brand-name .highlight {
        color: #0d6efd;
        -webkit-text-fill-color: #0d6efd;
        text-shadow: 0 0 20px rgba(13, 110, 253, 0.5);
    }
    
    .brand-tagline {
        font-size: 1.25rem;
        color: #9ca3af;
        margin: 0.5rem 0 0 0;
        letter-spacing: 1.3px;
        font-weight: 500;
    }
    
    /* Tags */
    .tags-row {
        display: flex;
        gap: 1.2rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .tag {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.9rem 1.6rem;
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.15) 0%, rgba(138, 43, 226, 0.1) 100%);
        border: 1.5px solid rgba(13, 110, 253, 0.4);
        border-radius: 25px;
        font-size: 1rem;
        font-weight: 600;
        color: #60a5fa;
        box-shadow: 0 0 20px rgba(13, 110, 253, 0.15);
        transition: all 0.3s ease;
    }
    
    .tag:hover {
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.25) 0%, rgba(138, 43, 226, 0.15) 100%);
        border-color: rgba(13, 110, 253, 0.6);
        box-shadow: 0 0 30px rgba(13, 110, 253, 0.25);
    }
    
    .tag-icon {
        font-size: 1.2rem;
    }
    
    /* Form Title - Hidden for banner layout */
    .form-title {
        display: none !important;
    }
    
    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin: 1.8rem 0 1.2rem 0;
        position: relative;
    }
    
    .section-icon {
        font-size: 1.6rem;
        flex-shrink: 0;
    }
    
    .section-text {
        font-size: 1.1rem;
        font-weight: 700;
        color: #fff;
        white-space: nowrap;
    }
    
    .section-line {
        flex-grow: 1;
        height: 2px;
        background: linear-gradient(to right, rgba(13, 110, 253, 0.3), transparent);
    }
    
    /* Field Labels */
    .field-label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 600;
        color: #d1d5db;
        margin-bottom: 0.6rem;
    }
    }
    
    .label-dot {
        width: 6px;
        height: 6px;
        background: linear-gradient(135deg, #0d6efd, #8a2be2);
        border-radius: 50%;
        display: inline-block;
    }
    
    /* Ratio Display */
    .ratio-display {
        background: rgba(10, 14, 39, 0.5);
        backdrop-filter: blur(10px);
        border: 1.5px solid rgba(13, 110, 253, 0.25);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        text-align: center;
    }
    
    .ratio-label {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        font-size: 0.85rem;
        font-weight: 600;
        color: #9ca3af;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    
    .transfer-icon {
        display: inline-block;
        width: 22px;
        height: 22px;
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%);
        border-radius: 4px;
        position: relative;
        animation: iconPulse 2s ease-in-out infinite;
    }
    
    @keyframes iconPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .transfer-icon::before,
    .transfer-icon::after {
        content: '→';
        position: absolute;
        color: #fff;
        font-size: 0.8rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .ratio-value {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    
    /* Warning Box */
    .warning-box {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.25);
        border-radius: 8px;
        padding: 0.5rem 0.7rem;
        color: #f87171;
        font-size: 0.7rem;
        font-weight: 600;
        margin: 0.4rem 0;
    }
    
    /* Time Badge */
    .time-badge {
        font-size: 1rem;
        font-weight: 600;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    /* Predict Button */
    .stButton > button {
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        padding: 1.2rem 2.5rem !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(13, 110, 253, 0.3) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover:not(:disabled) {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(13, 110, 253, 0.4) !important;
    }
    
    .stButton > button:disabled {
        background: #374151 !important;
        opacity: 0.5 !important;
    }
    
    /* Security Note */
    .security-note {
        text-align: center;
        color: #4a5568;
        font-size: 0.85rem;
        margin-top: 0.8rem;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .header-card {
            flex-direction: column;
            gap: 0.8rem;
            text-align: center;
        }
        .tags-row {
            justify-content: center;
        }
    }
    </style>
    """
    st.markdown(predict_css, unsafe_allow_html=True)


def render_header():
    """Render the animated header banner at the top."""
    header_html = """
    <div class="banner-header">
        <div class="header-card">
            <div class="logo-container">
                <div class="logo-outer-ring"></div>
                <div class="logo-inner-ring"></div>
                <div class="logo-core">🛡️</div>
            </div>
            <div>
                <div class="brand-name">
                    <span class="text-gradient">Transact</span><span class="highlight">Guard</span>
                </div>
                <div class="brand-tagline">AI Fraud Detection System</div>
            </div>
        </div>
        <div class="tags-row">
            <div class="tag"><span class="tag-icon">🧠</span> ML Powered</div>
            <div class="tag"><span class="tag-icon">⚡</span> Real-time</div>
            <div class="tag"><span class="tag-icon">🔐</span> Secure</div>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def start_form_wrapper():
    """Start the form wrapper container."""
    st.markdown("""
    <style>
    .form-container-wrapper {
        width: 100%;
        padding: 3.5rem 2rem 4rem 2rem;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        min-height: auto;
        background: linear-gradient(180deg, rgba(13, 110, 253, 0.08) 0%, rgba(138, 43, 226, 0.05) 50%, rgba(13, 110, 253, 0.04) 100%);
        box-shadow: inset 0 0 100px rgba(13, 110, 253, 0.15);
    }
    </style>
    <div class="form-container-wrapper">
    """, unsafe_allow_html=True)
    st.markdown('<div class="form-wrapper">', unsafe_allow_html=True)


def end_form_wrapper():
    """End the form wrapper container."""
    st.markdown('</div></div>', unsafe_allow_html=True)


def render_form_title(title="Transaction Analysis", subtitle="Enter transaction details for instant fraud detection"):
    """Render the form title with spinning globe."""
    form_title_html = f"""
    <div class="form-title">
        <h2>
            <span class="spinning-globe">🌐</span>
            {title}
        </h2>
        <p>{subtitle}</p>
    </div>
    """
    st.markdown(form_title_html, unsafe_allow_html=True)


def render_section_header(icon, text):
    """Render a section header with icon and divider line."""
    section_html = f"""
    <div class="section-header">
        <div class="section-icon">{icon}</div>
        <span class="section-text">{text}</span>
        <div class="section-line"></div>
    </div>
    """
    st.markdown(section_html, unsafe_allow_html=True)


def render_field_label(label):
    """Render a field label with animated dot."""
    label_html = f'<div class="field-label"><span class="label-dot"></span> {label}</div>'
    st.markdown(label_html, unsafe_allow_html=True)


def render_sidebar():
    """Render the sidebar navigation used across all pages."""
    with st.sidebar:
        st.markdown('<h3 style="color: var(--text-primary);">TransactGuard</h3>', unsafe_allow_html=True)
        
        if st.button('🏠 Home', use_container_width=True):
            st.switch_page('pages/01_Home.py')
            
        if st.button('📊 Predict', use_container_width=True):
            st.switch_page('pages/02_Predict.py')
            
        if st.button('📈 Results', use_container_width=True):
            st.switch_page('pages/03_Results.py')
            
        if st.button('📋 Data', use_container_width=True):
            st.switch_page('pages/04_Data.py')
            
        if st.button('ℹ️ About', use_container_width=True):
            st.switch_page('pages/05_About.py')
            
        st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size:12px;color:var(--text-secondary); text-align: center;">Built by Freshbuilders – SAIT</div>', unsafe_allow_html=True)