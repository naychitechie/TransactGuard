"""Styling helpers for TransactGuard Streamlit app.

Provides `apply_dark_theme` and `render_sidebar` helpers that pages can
import. Ensures Streamlit is available and avoids ImportError when a page
imports `render_sidebar`.
"""
import streamlit as st

def apply_dark_theme():
    dark_theme_css = """
    <style>
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

    /* hide the top-right hamburger menu (MainMenu) and footer */
    MainMenu { visibility: hidden }
    footer { visibility: hidden !important; }

    /* optional: hide the top toolbar if present */
    [data-testid="stToolbar"] { visibility: hidden !important; }

    /* Hide Streamlit's built-in page/navigation list inside the left sidebar */
    [data-testid="stSidebar"] nav,
    [data-testid="stSidebar"] [role="navigation"],
    [data-testid="stSidebar"] ul,
    [data-testid="stSidebar"] .css-1d391kg {  /* fallback class name in some versions */
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

    /* keep header background consistent */
    header, [data-testid="stHeader"] {
        background-color: var(--dark-bg) !important;
        color: var(--text-primary) !important;
    }

    /* Ensure the main app and body use the dark background */
    [data-testid="stAppViewContainer"] { background-color: var(--dark-bg) !important; }
    main, body, .appview-container, .reportview-container { background-color: var(--dark-bg) !important; }
    body { min-height: 100vh; }

    .card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        color: var(--text-secondary) !important;
    }

    /* Sidebar navigation styles */
    .nav-container {
        display: flex;
        flex-direction: column;
        gap: 8px;
        padding: 8px 4px;
    }
    .nav-button {
        display: block;
        width: 100%;
        text-align: left;
        background-color: transparent;
        border: 1px solid var(--border-color);
        color: var(--text-primary);
        padding: 10px 12px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 14px;
    }
    .nav-button:hover { border-color: #2563eb; color: #2563eb; background-color: rgba(255,255,255,0.02); }

    /* Apply configurable sidebar background */
    [data-testid="stSidebar"] { background-color: var(--sidebar-bg) !important; }

    .section-title {
        font-size: 20px;
        margin-top: 20px;
        margin-bottom: 8px;
        color: var(--text-secondary) !important;
    }
# 2563eb
    .button-primary {
        background-color: #2F80ED;
        color: #ffffff;
        border: none;
        padding: 10px 16px;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
    }

    /* Make Streamlit native buttons match the .button-primary style */
    div.stButton > button {
            # background-color: #0F1D40 !important;
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

    .hero-section { text-align: center; padding: 24px 0; }
    .hero-title { font-size: 36px; margin: 8px 0; color: var(--text-primary) !important; opacity: 1 !important; }

    /* Widget tweaks for readability */
    div.stTextInput > div > div > input,
    div.stNumberInput > div > input,
    div.stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ccc !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
    }

    </style>
    """
    st.markdown(dark_theme_css, unsafe_allow_html=True)


# def render_sidebar():
#     nav_html = """
#     <div class="nav-container">
#         <a class="nav-button" href="?page=Home">🏠 Home</a>
#         <a class="nav-button" href="?page=Predict">📊 Prediction</a>
#         <a class="nav-button" href="?page=Results">📈 Results</a>
#         <a class="nav-button" href="?page=Data">📋 Data</a>
#         <a class="nav-button" href="?page=About">ℹ️ About</a>
#     </div>
#     """
#     st.markdown(nav_html, unsafe_allow_html=True)

def render_sidebar():
    """Render a simple sidebar used across app pages.

    This function intentionally keeps behavior minimal to avoid coupling
    with page navigation logic. Pages can call it to show consistent
    branding and quick links.
    """
    with st.sidebar:
        st.markdown('<h3 style="color: var(--text-primary); margin:0 0 6px 0;">TransactGuard</h3>', unsafe_allow_html=True)
        if st.button('🏠 Home'):
            # try:
                st.switch_page('pages/01_Home.py')
            # except Exception:
            #     # fallback: set query param for older Streamlit versions
            #     st.experimental_set_query_params(page='Home')
        if st.button('📊 Predict'):
            # try:
                st.switch_page('pages/02_Predict.py')
            # except Exception:
            #     st.experimental_set_query_params(page='Predict')
        if st.button('📈 Results'):
            # try:
                st.switch_page('pages/03_Results.py')
            # except Exception:
            #     st.experimental_set_query_params(page='Results')
        if st.button('📋 Data'):
            # try:
                st.switch_page('pages/04_Data.py')
            # except Exception:
            #     st.experimental_set_query_params(page='Data')
        if st.button('ℹ️ About'):
            # try:
                st.switch_page('pages/05_About.py')
            # except Exception:
            #     st.experimental_set_query_params(page='About')
        st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size:12px;color:var(--text-secondary);">Built by Freshbuilders — SAIT</div>', unsafe_allow_html=True)