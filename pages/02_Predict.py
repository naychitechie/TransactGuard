"""Predict page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar
from src.prediction_service import get_fraud_prediction

st.set_page_config(page_title="Predict - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()

# Add ONLY form-related CSS - ABSOLUTELY NO SIDEBAR STYLING
st.markdown("""
<style>
    /* Main container - make it wider and better spaced */
    .block-container {
        max-width: 1600px !important;
        padding: 2.5rem 3rem !important;
    }
    
    /* Section Headers - MUCH MUCH BIGGER */
    .section-header {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin: 2.5rem 0 1.8rem 0;
    }
    
    .section-icon {
        width: 55px;
        height: 55px;
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.2) 0%, rgba(138, 43, 226, 0.2) 100%);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        flex-shrink: 0;
        animation: iconGlow 3s ease-in-out infinite;
    }
    
    @keyframes iconGlow {
        0%, 100% { 
            box-shadow: 0 0 15px rgba(13, 110, 253, 0.3);
        }
        50% { 
            box-shadow: 0 0 25px rgba(138, 43, 226, 0.5);
        }
    }
    
    .section-text {
        color: #e2e8f0;
        font-size: 1.6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        white-space: nowrap;
    }
    
    .section-line {
        flex: 1;
        height: 3px;
        background: linear-gradient(90deg, rgba(13, 110, 253, 0.4), transparent);
        margin-left: 1.5rem;
    }
    
    /* Input Labels - MUCH MUCH BIGGER */
    .field-label {
        color: #8892b0;
        font-size: 1.4rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    
    .label-dot {
        width: 12px;
        height: 12px;
        background: linear-gradient(135deg, #0d6efd, #8a2be2);
        border-radius: 4px;
        flex-shrink: 0;
        animation: dotPulse 2s ease-in-out infinite;
    }
    
    @keyframes dotPulse {
        0%, 100% { 
            box-shadow: 0 0 5px rgba(13, 110, 253, 0.5);
        }
        50% { 
            box-shadow: 0 0 10px rgba(138, 43, 226, 0.8);
        }
    }
    
    /* Number Input - FORCE EXACT SAME SIZE AS SELECTBOX WITH STRONG GLOW */
    section[data-testid="stMain"] .stNumberInput {
        height: auto !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div {
        height: auto !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div {
        height: 70px !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Give the NUMBER input container the exact same visual treatment as the selectbox
       so the glow animation, border, padding and background match perfectly */
    section[data-testid="stMain"] .stNumberInput > div > div {
        background: rgba(10, 14, 39, 0.95) !important;
        border: 2px solid rgba(13, 110, 253, 0.4) !important;
        border-radius: 16px !important;
        transition: all 0.25s ease !important;
        min-height: 70px !important;
        height: 70px !important;
        padding: 0 1.5rem !important;
        /* stronger base glow so it visually matches the selectbox */
        box-shadow: 
            0 0 30px rgba(13, 110, 253, 0.45),
            inset 0 0 28px rgba(13, 110, 253, 0.08) !important;
        display: flex !important;
        align-items: center !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        overflow: hidden !important;
        animation: selectGlowStrong 3s ease-in-out infinite;
    }
    /* Make the inner input element visually transparent so the decorated container
       (with its animation) is visible exactly like the selectbox. Keep text sizing
       and alignment inside the container. */
    section[data-testid="stMain"] .stNumberInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 12px !important;
        color: #fff !important;
        /* more right padding so the visible text doesn't overlap the steppers */
        padding: 0 3.5rem 0 1rem !important;
        font-size: 1.6rem !important;
        font-weight: 600 !important;
        transition: all 0.15s ease !important;
        min-height: 70px !important;
        height: 70px !important;
        width: 100% !important;
        line-height: 1.2 !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        background-clip: padding-box !important;
        text-align: left !important;
        vertical-align: middle !important;
        display: flex !important;
        align-items: center !important;
    }

    /* Force all nested elements in number input to show the large font */
    section[data-testid="stMain"] .stNumberInput input,
    section[data-testid="stMain"] .stNumberInput span,
    section[data-testid="stMain"] .stNumberInput > div span {
        font-size: 2rem !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
    }

    /* Ensure any inner wrapper that Streamlit might add is transparent too */
    section[data-testid="stMain"] .stNumberInput > div > div > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        height: 100% !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
        font-size: 4rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
    }

    /* Force ALL inner descendants to be transparent so no inner dark block shows */
    section[data-testid="stMain"] .stNumberInput > div > div * {
        background: transparent !important;
        background-image: none !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* Style the stepper / control buttons to visually match the selectbox container
       and align height so the whole control reads as a single element. */
    section[data-testid="stMain"] .stNumberInput > div > div button,
    section[data-testid="stMain"] .stNumberInput button {
        /* Make steppers visually flat and let the container show through */
        background: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-left: none !important;
        height: 100% !important;
        min-width: 56px !important;
        padding: 0 0.8rem !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Make the button icons (arrows) use the same accent color */
    section[data-testid="stMain"] .stNumberInput > div > div button svg,
    section[data-testid="stMain"] .stNumberInput button svg {
        /* mute the icon color so + / - aren't highlighted */
        fill: #cbd5e1 !important;
        width: 18px !important;
        height: 18px !important;
        opacity: 0.95 !important;
    }

    /* Prevent hover from adding a blue highlight to the steppers */
    section[data-testid="stMain"] .stNumberInput > div > div button:hover,
    section[data-testid="stMain"] .stNumberInput button:hover {
        background: rgba(10,14,39,0.95) !important;
        box-shadow: none !important;
        transform: none !important;
        border-left: 1px solid rgba(13, 110, 253, 0.06) !important;
    }
    
    @keyframes inputGlowStrong {
        0%, 100% { 
            box-shadow: 
                0 0 25px rgba(13, 110, 253, 0.3),
                inset 0 0 20px rgba(13, 110, 253, 0.05);
            border-color: rgba(13, 110, 253, 0.4);
        }
        50% { 
            box-shadow: 
                0 0 40px rgba(138, 43, 226, 0.5),
                inset 0 0 30px rgba(138, 43, 226, 0.1);
            border-color: rgba(138, 43, 226, 0.6);
        }
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div > input:hover {
        border-color: rgba(13, 110, 253, 0.7) !important;
        box-shadow: 
            0 0 45px rgba(13, 110, 253, 0.5),
            inset 0 0 25px rgba(13, 110, 253, 0.1) !important;
        animation: none !important;
    }

    /* Mirror hover/focus behavior for number input container */
    section[data-testid="stMain"] .stNumberInput > div > div:hover {
        border-color: rgba(13, 110, 253, 0.7) !important;
        box-shadow: 
            0 0 45px rgba(13, 110, 253, 0.5),
            inset 0 0 25px rgba(13, 110, 253, 0.1) !important;
        animation: none !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div:focus-within {
        border-color: #0d6efd !important;
        box-shadow: 
            0 0 50px rgba(13, 110, 253, 0.7),
            inset 0 0 30px rgba(13, 110, 253, 0.15) !important;
        animation: none !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div > input:focus {
        border-color: #0d6efd !important;
        box-shadow: 
            0 0 50px rgba(13, 110, 253, 0.7),
            inset 0 0 30px rgba(13, 110, 253, 0.15) !important;
        animation: none !important;
    }

    /* Aggressive overrides: clear any nested wrapper or input backgrounds / shadows
       (some Streamlit versions insert inner wrappers with their own backgrounds).
       This forces the inner area to be transparent so the outer animated container
       is what's visible. Also remove native spinner appearance. */
    section[data-testid="stMain"] .stNumberInput input[type="number"],
    section[data-testid="stMain"] .stNumberInput input,
    section[data-testid="stMain"] .stNumberInput > div > div > div,
    section[data-testid="stMain"] .stNumberInput > div > div > div > div,
    section[data-testid="stMain"] .stNumberInput > div > div > div > span {
        background: transparent !important;
        background-image: none !important;
        box-shadow: none !important;
        border: none !important;
        -webkit-appearance: none !important;
        -moz-appearance: textfield !important;
        appearance: none !important;
        color: #fff !important;
        height: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Remove default webkit spin buttons so styling is consistent */
    section[data-testid="stMain"] .stNumberInput input::-webkit-outer-spin-button,
    section[data-testid="stMain"] .stNumberInput input::-webkit-inner-spin-button {
        -webkit-appearance: none !important;
        margin: 0 !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
    }

    /* Firefox: remove number input spinbox */
    section[data-testid="stMain"] .stNumberInput input[type="number"] {
        -moz-appearance: textfield !important;
    }
    
    /* Selectbox Container Styling - EXACT SAME SIZE WITH STRONG GLOW */
    section[data-testid="stMain"] .stSelectbox > div > div {
        background: rgba(10, 14, 39, 0.95) !important;
        border: 2px solid rgba(13, 110, 253, 0.4) !important;
        border-radius: 16px !important;
        transition: all 0.25s ease !important;
        min-height: 70px !important;
        height: 70px !important;
        padding: 0 1.5rem !important;
        box-shadow: 
            0 0 30px rgba(13, 110, 253, 0.45),
            inset 0 0 28px rgba(13, 110, 253, 0.08) !important;
        display: flex !important;
        align-items: center !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        animation: selectGlowStrong 3s ease-in-out infinite;
    }
    
    @keyframes selectGlowStrong {
        0%, 100% { 
            box-shadow: 
                0 0 30px rgba(13, 110, 253, 0.45),
                inset 0 0 28px rgba(13, 110, 253, 0.08);
            border-color: rgba(13, 110, 253, 0.6);
        }
        50% { 
            box-shadow: 
                0 0 60px rgba(138, 43, 226, 0.65),
                inset 0 0 40px rgba(138, 43, 226, 0.12);
            border-color: rgba(138, 43, 226, 0.7);
        }
    }
    
    section[data-testid="stMain"] .stSelectbox > div > div:hover {
        border-color: rgba(13, 110, 253, 0.7) !important;
        box-shadow: 
            0 0 45px rgba(13, 110, 253, 0.5),
            inset 0 0 25px rgba(13, 110, 253, 0.1) !important;
        animation: none !important;
    }
    
    section[data-testid="stMain"] .stSelectbox > div > div:focus-within {
        border-color: #0d6efd !important;
        box-shadow: 
            0 0 50px rgba(13, 110, 253, 0.7),
            inset 0 0 30px rgba(13, 110, 253, 0.15) !important;
        animation: none !important;
    }
    
    /* Fix for selected text visibility - GIANT TEXT - MATCH NUMBER INPUT */
    section[data-testid="stMain"] .stSelectbox [data-baseweb="select"] > div,
    section[data-testid="stMain"] .stSelectbox [data-baseweb="select"] span,
    section[data-testid="stMain"] .stSelectbox [role="button"] > div,
    section[data-testid="stMain"] .stSelectbox [role="button"] span,
    section[data-testid="stMain"] .stSelectbox [data-baseweb="select"] div[class*="singleValue"] {
        color: #ffffff !important;
        font-size: 1.6rem !important;
        font-weight: 600 !important;
        padding: 0 !important;
        line-height: 1.2 !important;
        margin: 0 !important;
    }
    
    /* Dropdown arrow - BIGGER AND ANIMATED */
    section[data-testid="stMain"] .stSelectbox svg {
        fill: #0d6efd !important;
        width: 32px !important;
        height: 32px !important;
        filter: drop-shadow(0 4px 12px rgba(13,110,253,0.18)) !important;
        transition: transform 0.2s ease !important;
    }
    
    section[data-testid="stMain"] .stSelectbox > div > div:hover svg {
        transform: scale(1.08) !important;
    }
    
    /* Dropdown Menu - POLISHED WITH GLOW */
    div[data-baseweb="menu"] {
        background: linear-gradient(180deg, rgba(10,14,39,0.98), rgba(10,14,39,0.96)) !important;
        border: 2px solid rgba(13, 110, 253, 0.35) !important;
        border-radius: 16px !important;
        box-shadow: 0 0 35px rgba(13, 110, 253, 0.28), inset 0 4px 12px rgba(13,110,253,0.04) !important;
        backdrop-filter: blur(2px);
        margin-top: 8px;
    }
    
    div[data-baseweb="menu"] li {
        color: #e2e8f0 !important;
        padding: 1.2rem 1.8rem !important;
        font-weight: 500 !important;
        font-size: 1.6rem !important;
        transition: all 0.15s ease !important;
        border-bottom: 1px solid rgba(13, 110, 253, 0.06) !important;
        margin: 0.4rem 0.8rem !important;
        border-radius: 8px !important;
    }
    
    div[data-baseweb="menu"] li:last-child {
        border-bottom: none !important;
    }
    
    div[data-baseweb="menu"] li:hover {
        background: linear-gradient(90deg, rgba(13, 110, 253, 0.22), rgba(138, 43, 226, 0.12)) !important;
        box-shadow: inset 0 0 20px rgba(13, 110, 253, 0.08) !important;
        color: #ffffff !important;
        transform: translateX(4px);
    }
    
    /* Slider Styling - BIGGER WITH GLOW */
    section[data-testid="stMain"] .stSlider > div > div > div {
        background: rgba(13, 110, 253, 0.15) !important;
        height: 12px !important;
        border-radius: 12px !important;
        box-shadow: 0 0 15px rgba(13, 110, 253, 0.2) !important;
    }
    
    section[data-testid="stMain"] .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #0d6efd, #8a2be2) !important;
        box-shadow: 0 0 20px rgba(13, 110, 253, 0.4) !important;
    }
    
    section[data-testid="stMain"] .stSlider [role="slider"] {
        background: #fff !important;
        width: 32px !important;
        height: 32px !important;
        border: 5px solid #0d6efd !important;
        box-shadow: 0 0 25px rgba(13, 110, 253, 0.6) !important;
        animation: sliderGlow 2s ease-in-out infinite;
    }
    
    @keyframes sliderGlow {
        0%, 100% { 
            box-shadow: 0 0 25px rgba(13, 110, 253, 0.6);
        }
        50% { 
            box-shadow: 0 0 35px rgba(138, 43, 226, 0.8);
        }
    }
    
    /* Time Badge - GIANT TEXT WITH GLOW */
    .time-badge {
        background: rgba(13, 110, 253, 0.12);
        border: 2px solid rgba(13, 110, 253, 0.3);
        border-radius: 14px;
        padding: 1.3rem 2rem;
        text-align: center;
        margin-top: 1.2rem;
        font-weight: 700;
        font-size: 2.5rem;
        box-shadow: 0 0 20px rgba(13, 110, 253, 0.2);
        animation: badgeGlow 3s ease-in-out infinite;
    }
    
    @keyframes badgeGlow {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(13, 110, 253, 0.2);
        }
        50% { 
            box-shadow: 0 0 30px rgba(138, 43, 226, 0.4);
        }
    }
    
    /* Slider Label - BIGGER TEXT */
    section[data-testid="stMain"] .stSlider > label {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
    }
    
    section[data-testid="stMain"] .stSlider span {
        font-size: 1.6rem !important;
        font-weight: 600 !important;
    }
    
    /* Ratio Display Card - GIANT WITH GLOW */
    .ratio-display {
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.12) 0%, rgba(138, 43, 226, 0.12) 100%);
        border: 2px solid rgba(13, 110, 253, 0.3);
        border-radius: 24px;
        padding: 3rem;
        margin: 3rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 40px rgba(13, 110, 253, 0.2);
        animation: cardGlow 4s ease-in-out infinite;
    }
    
    @keyframes cardGlow {
        0%, 100% { 
            box-shadow: 0 0 40px rgba(13, 110, 253, 0.2);
            border-color: rgba(13, 110, 253, 0.3);
        }
        50% { 
            box-shadow: 0 0 50px rgba(138, 43, 226, 0.4);
            border-color: rgba(138, 43, 226, 0.4);
        }
    }
    
    .ratio-display::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .ratio-label {
        color: #8892b0;
        font-size: 1.6rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2.5px;
        margin-bottom: 1.2rem;
    }
    
    .ratio-value {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        text-shadow: 0 0 30px rgba(13, 110, 253, 0.3);
    }
    
    /* Warning Box - GIANT TEXT WITH GLOW */
    .warning-box {
        background: rgba(239, 68, 68, 0.12);
        border: 2px solid rgba(239, 68, 68, 0.3);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        color: #f87171;
        font-size: 1.6rem;
        font-weight: 600;
        margin: 2.5rem 0;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.2);
        animation: warningPulse 2s ease-in-out infinite;
    }
    
    @keyframes warningPulse {
        0%, 100% { 
            box-shadow: 0 0 25px rgba(239, 68, 68, 0.2);
        }
        50% { 
            box-shadow: 0 0 35px rgba(239, 68, 68, 0.4);
        }
    }
    
    /* Button Styling - GIANT TEXT WITH GLOW ANIMATION */
    section[data-testid="stMain"] .stButton > button {
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        padding: 1.5rem 3rem !important;
        border-radius: 18px !important;
        border: none !important;
        box-shadow: 0 12px 35px rgba(13, 110, 253, 0.4) !important;
        text-transform: uppercase !important;
        letter-spacing: 5px !important;
        transition: all 0.3s ease !important;
        min-height: 80px !important;
        animation: buttonGlow 3s ease-in-out infinite;
        line-height: 1.1 !important;
    }
    
    section[data-testid="stMain"] .stButton > button * {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
    }
    
    @keyframes buttonGlow {
        0%, 100% { 
            box-shadow: 0 12px 35px rgba(13, 110, 253, 0.4);
        }
        50% { 
            box-shadow: 0 15px 45px rgba(138, 43, 226, 0.6);
        }
    }
    
    section[data-testid="stMain"] .stButton > button:hover:not(:disabled) {
        transform: translateY(-3px) !important;
        box-shadow: 0 18px 50px rgba(13, 110, 253, 0.7) !important;
    }
    
    section[data-testid="stMain"] .stButton > button:disabled {
        background: linear-gradient(135deg, #374151 0%, #4b5563 100%) !important;
        opacity: 0.6 !important;
        cursor: not-allowed !important;
        animation: none !important;
    }
    
    /* Add spacing between columns */
    .row-widget.stHorizontal {
        gap: 2.5rem !important;
    }
    /* Page heading styles */
    .page-heading {
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1.2rem;
        letter-spacing: 0.4px;
        color: #ffffff;
        position: relative;
        display: inline-block;
        width: 100%;
    }
    .page-heading::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 160px;
        height: 3px;
        background: linear-gradient(90deg, #0d6efd, #8a2be2);
        border-radius: 3px;
        box-shadow: 0 6px 16px rgba(13, 110, 253, 0.2);
    }
    .page-subtext {
        text-align: center;
        color: #9fb0c8;
        font-size: 1.02rem;
        margin-bottom: 1.6rem;
        font-weight: 600;
    }
    /* Full-page overlay loader (TransactGuard) - polished glass card */
    .tg-overlay {
        position: fixed !important;
        inset: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        z-index: 9999 !important;
        background: linear-gradient(180deg, rgba(2,6,23,0.86), rgba(2,6,23,0.94));
        backdrop-filter: blur(6px) saturate(120%);
    }

    .tg-card {
        width: min(920px, calc(100% - 64px));
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.04);
        border-radius: 18px;
        padding: 2.25rem 2.5rem;
        box-shadow: 0 18px 60px rgba(2,6,23,0.6), 0 8px 36px rgba(13,110,253,0.06);
        display: flex; flex-direction: column; align-items: center; gap: 1rem;
    }

    .tg-loader-wrap { display:flex; align-items:center; gap:1.25rem; }

    .tg-loader {
        width: 96px; height: 96px; border-radius: 50%;
        background: conic-gradient(from 0deg, #0d6efd, #8a2be2, #6b46c1);
        display:flex; align-items:center; justify-content:center; position: relative;
        box-shadow: 0 10px 40px rgba(13,110,253,0.22), inset 0 -6px 18px rgba(0,0,0,0.25);
        animation: tg-spin 1.8s linear infinite;
    }

    .tg-loader-inner { width:62px; height:62px; border-radius:50%; background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)); display:flex; align-items:center; justify-content:center; font-size:34px; }
    @keyframes tg-spin { to { transform: rotate(360deg); } }

    .tg-title { font-size: 1.6rem; font-weight: 800; margin: 0.6rem 0 0.2rem 0; letter-spacing: 0.6px; background: linear-gradient(90deg,#fff,#cbd5e1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .tg-sub { color: #cbd5e1; font-size: 1rem; margin: 0; }

    .tg-progress { margin-top: 1rem; width: 84%; height: 12px; background: rgba(255,255,255,0.04); border-radius: 10px; overflow: hidden; }
    .tg-progress-bar { height: 100%; width: 0%; background: linear-gradient(90deg,#0d6efd,#8a2be2); border-radius: 10px; box-shadow: 0 8px 22px rgba(13,110,253,0.22); animation: tg-progress-anim 4s linear forwards; }
    @keyframes tg-progress-anim { from { width: 0%; } to { width: 100%; } }

    .tg-dots{ margin-top: 0.8rem; }
    .tg-dots span{ display:inline-block; width:10px; height:10px; margin: 0 6px; background: #fff; border-radius:50%; opacity:0.14; box-shadow:0 6px 18px rgba(13,110,253,0.06); animation: tg-dots 1s infinite; }
    .tg-dots span:nth-child(1){ animation-delay: 0s } .tg-dots span:nth-child(2){ animation-delay: 0.14s } .tg-dots span:nth-child(3){ animation-delay: 0.28s }
    @keyframes tg-dots{ 0%{opacity:0.14; transform: translateY(0)} 50%{opacity:1; transform: translateY(-8px)} 100%{opacity:0.14; transform: translateY(0)} }

    /* responsive */
    @media (max-width: 640px) {
        .tg-card { padding: 1.25rem; }
        .tg-title { font-size: 1.2rem; }
        .tg-loader { width:72px; height:72px; }
        .tg-loader-inner { width:48px; height:48px; font-size:22px; }
        .tg-progress { width: 92%; }
    }

</style>
""", unsafe_allow_html=True)

# Rest of the code remains the same...
# Page Title - GIANT
st.markdown('<div style="text-align:center;"><div class="page-heading">Enter Transaction Details</div></div>', unsafe_allow_html=True)

# Transaction Details Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">💳</div>
    <span class="section-text">Transaction Details</span>
    <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Transaction Amount</div>', unsafe_allow_html=True)
    transaction_amount = st.number_input("Transaction Amount", min_value=0.0, label_visibility="collapsed", key="amt", step=10.0, format="%.2f")

with col2:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Sender Initial Balance</div>', unsafe_allow_html=True)
    sender_init_balance = st.number_input("Sender Initial Balance", min_value=0.0, label_visibility="collapsed", key="sb", step=100.0, format="%.2f")

# Calculate and display ratio in real-time
if sender_init_balance > 0:
    amount_to_sender_balance_ratio = transaction_amount / sender_init_balance
    
    # Validation: Check if transaction amount exceeds sender balance
    if transaction_amount > sender_init_balance:
        st.markdown(f'<div class="warning-box">⚠️ Transaction amount cannot exceed sender balance!</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="ratio-display">
            <div class="ratio-label">💸 Amount to Sender Balance Ratio</div>
            <div class="ratio-value">{amount_to_sender_balance_ratio:.4f}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    amount_to_sender_balance_ratio = 0.0
    st.markdown(f'<div class="ratio-display"><div class="ratio-label">💸 Amount to Sender Balance Ratio</div><div class="ratio-value">0.0000</div></div>', unsafe_allow_html=True)

# Account Balance Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">💰</div>
    <span class="section-text">Account Information</span>
    <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")
with col3:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Sender Behavior ID</div>', unsafe_allow_html=True)
    sender_behavior_id = st.selectbox(
        "Sender Behavior ID", 
        options=[1, 2, 3, 4, 5], 
        label_visibility="collapsed",
        index=0,
        key="sender_behavior"
    )

with col4:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Receiver Initial Balance</div>', unsafe_allow_html=True)
    receiver_initial_balance = st.number_input("Receiver Initial Balance", min_value=0.0, label_visibility="collapsed", key="rb", step=100.0, format="%.2f")

# Transaction Timing Section
st.markdown("""
<div class="section-header">
    <div class="section-icon">🕐</div>
    <span class="section-text">Transaction Timing</span>
    <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

col5, col6 = st.columns(2, gap="large")
with col5:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Day of Week</div>', unsafe_allow_html=True)
    day_of_week_name = st.selectbox(
        "Day of the Week", 
        options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 
        label_visibility="collapsed",
        index=0,
        key="day_of_week_select"
    )
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week_name)

with col6:
    st.markdown('<div class="field-label"><span class="label-dot"></span> Hour of Transaction</div>', unsafe_allow_html=True)
    hour = st.slider("hour", min_value=0, max_value=23, value=14, label_visibility="collapsed", key="hour_slider")
    
    # Determine time period and color
    if 5 <= hour < 12:
        period, color = "Morning", "#fbbf24"
    elif 12 <= hour < 17:
        period, color = "Afternoon", "#f59e0b"
    elif 17 <= hour < 21:
        period, color = "Evening", "#a855f7"
    else:
        period, color = "Night", "#3b82f6"
    
    st.markdown(f'<div class="time-badge" style="color: {color};">{hour:02d}:00 • {period}</div>', unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Disable predict button if transaction amount exceeds sender balance
predict_disabled = transaction_amount > sender_init_balance if sender_init_balance > 0 else False

if st.button("Predict Fraud", use_container_width=True, disabled=predict_disabled):
        # Render a full-page styled overlay while 'analyzing' runs
        overlay_placeholder = st.empty()
        overlay_html = '''
                <div class="tg-overlay">
                    <div class="tg-card" role="dialog" aria-live="polite">
                        <div class="tg-loader-wrap">
                            <div class="tg-loader"><div class="tg-loader-inner">🔮</div></div>
                            <div style="text-align:left;">
                                <div class="tg-title">Analyzing transaction...</div>
                                <div class="tg-sub">Running a comprehensive fraud analysis — this usually takes a few seconds.</div>
                            </div>
                        </div>
                        <div class="tg-progress"><div class="tg-progress-bar"></div></div>
                        <div class="tg-dots" aria-hidden="true"><span></span><span></span><span></span></div>
                    </div>
                </div>
                '''
        overlay_placeholder.markdown(overlay_html, unsafe_allow_html=True)

        import time
        time.sleep(4)

        # Execute prediction and navigate to results
        result = get_fraud_prediction(
                                        transaction_amount, 
                                        sender_init_balance,
                                        sender_behavior_id,
                                        receiver_initial_balance,
                                        int(hour),
                                        day_of_week,
                                        amount_to_sender_balance_ratio
                                )

    
    if st.button("Predict", use_container_width=True):
        result = get_fraud_prediction(transaction_amount, sender_balance, receiver_balance, sender_behavior_id, day_of_week, int(hour))
        st.session_state.prediction_result = result
        # remove overlay before switching
        overlay_placeholder.empty()
        st.switch_page("pages/03_Results.py")