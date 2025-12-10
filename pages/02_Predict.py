"""Predict page"""
import streamlit as st
from src.styles import apply_dark_theme, render_sidebar
from src.prediction_service import get_fraud_prediction

st.set_page_config(page_title="Predict - TransactGuard", layout="wide", initial_sidebar_state="expanded")
apply_dark_theme()
render_sidebar()
predict_disabled = True

# Add ONLY form-related CSS - ABSOLUTELY NO SIDEBAR STYLING
st.markdown("""
<style>
    /* Main container - use viewport units for consistent sizing */
    .block-container {
        max-width: min(1200px, 90vw) !important;
        padding: 3vh 2vw 2vh 2vw !important;
    }
    
    /* Section Headers - responsive sizing */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.8vw;
        margin: 1.5vh 0 1vh 0;
    }
    
    .section-icon {
        width: clamp(32px, 2.5vw, 38px);
        height: clamp(32px, 2.5vw, 38px);
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.2) 0%, rgba(138, 43, 226, 0.2) 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: clamp(1rem, 1.1vw, 1.2rem);
        flex-shrink: 0;
        animation: iconGlow 3s ease-in-out infinite;
    }
    
    @keyframes iconGlow {
        0%, 100% { 
            box-shadow: 0 0 12px rgba(13, 110, 253, 0.25);
        }
        50% { 
            box-shadow: 0 0 20px rgba(138, 43, 226, 0.4);
        }
    }
    
    .section-text {
        color: #e2e8f0;
        font-size: clamp(0.9rem, 1vw, 1.05rem);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        white-space: nowrap;
    }
    
    .section-line {
        flex: 1;
        height: 2px;
        background: linear-gradient(90deg, rgba(13, 110, 253, 0.35), transparent);
        margin-left: 0.8vw;
    }
    
    /* Input Labels - responsive sizing */
    .field-label {
        color: #8892b0;
        font-size: clamp(0.8rem, 0.85vw, 0.9rem);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.5vh;
        display: flex;
        align-items: center;
        gap: 0.3vw;
    }
    
    .label-dot {
        width: 7px;
        height: 7px;
        background: linear-gradient(135deg, #0d6efd, #8a2be2);
        border-radius: 2px;
        flex-shrink: 0;
        animation: dotPulse 2s ease-in-out infinite;
    }
    
    @keyframes dotPulse {
        0%, 100% { 
            box-shadow: 0 0 4px rgba(13, 110, 253, 0.4);
        }
        50% { 
            box-shadow: 0 0 8px rgba(138, 43, 226, 0.7);
        }
    }
    
    /* Number Input - responsive height */
    section[data-testid="stMain"] .stNumberInput {
        height: auto !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div {
        height: auto !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div {
        height: clamp(42px, 4vh, 48px) !important;
        display: flex !important;
        align-items: center !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div {
        background: rgba(10, 14, 39, 0.95) !important;
        border: 2px solid rgba(13, 110, 253, 0.35) !important;
        border-radius: 10px !important;
        transition: all 0.25s ease !important;
        min-height: clamp(42px, 4vh, 48px) !important;
        height: clamp(42px, 4vh, 48px) !important;
        padding: 0 0.9vw !important;
        box-shadow: 
            0 0 20px rgba(13, 110, 253, 0.3),
            inset 0 0 15px rgba(13, 110, 253, 0.05) !important;
        display: flex !important;
        align-items: center !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        overflow: hidden !important;
        animation: selectGlowStrong 3s ease-in-out infinite;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        color: #fff !important;
        padding: 0 2.2vw 0 0.6vw !important;
        font-size: clamp(0.9rem, 0.95vw, 1rem) !important;
        font-weight: 600 !important;
        transition: all 0.15s ease !important;
        min-height: clamp(42px, 4vh, 48px) !important;
        height: clamp(42px, 4vh, 48px) !important;
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

    section[data-testid="stMain"] .stNumberInput input,
    section[data-testid="stMain"] .stNumberInput span,
    section[data-testid="stMain"] .stNumberInput > div span {
        font-size: clamp(0.9rem, 0.95vw, 1rem) !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        height: 100% !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 !important;
        font-size: clamp(0.9rem, 0.95vw, 1rem) !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div * {
        background: transparent !important;
        background-image: none !important;
        box-shadow: none !important;
        border: none !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div button,
    section[data-testid="stMain"] .stNumberInput button {
        background: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-left: none !important;
        height: 100% !important;
        min-width: clamp(35px, 3vw, 40px) !important;
        padding: 0 0.5vw !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div button svg,
    section[data-testid="stMain"] .stNumberInput button svg {
        fill: #cbd5e1 !important;
        width: 12px !important;
        height: 12px !important;
        opacity: 0.95 !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div button:hover,
    section[data-testid="stMain"] .stNumberInput button:hover {
        background: rgba(10,14,39,0.95) !important;
        box-shadow: none !important;
        transform: none !important;
        border-left: 1px solid rgba(13, 110, 253, 0.05) !important;
    }
    
    @keyframes inputGlowStrong {
        0%, 100% { 
            box-shadow: 
                0 0 18px rgba(13, 110, 253, 0.22),
                inset 0 0 12px rgba(13, 110, 253, 0.03);
            border-color: rgba(13, 110, 253, 0.35);
        }
        50% { 
            box-shadow: 
                0 0 30px rgba(138, 43, 226, 0.4),
                inset 0 0 20px rgba(138, 43, 226, 0.06);
            border-color: rgba(138, 43, 226, 0.55);
        }
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div > input:hover {
        border-color: rgba(13, 110, 253, 0.65) !important;
        box-shadow: 
            0 0 35px rgba(13, 110, 253, 0.4),
            inset 0 0 18px rgba(13, 110, 253, 0.07) !important;
        animation: none !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div:hover {
        border-color: rgba(13, 110, 253, 0.65) !important;
        box-shadow: 
            0 0 35px rgba(13, 110, 253, 0.4),
            inset 0 0 18px rgba(13, 110, 253, 0.07) !important;
        animation: none !important;
    }

    section[data-testid="stMain"] .stNumberInput > div > div:focus-within {
        border-color: #0d6efd !important;
        box-shadow: 
            0 0 40px rgba(13, 110, 253, 0.55),
            inset 0 0 22px rgba(13, 110, 253, 0.1) !important;
        animation: none !important;
    }
    
    section[data-testid="stMain"] .stNumberInput > div > div > input:focus {
        border-color: #0d6efd !important;
        box-shadow: 
            0 0 40px rgba(13, 110, 253, 0.55),
            inset 0 0 22px rgba(13, 110, 253, 0.1) !important;
        animation: none !important;
    }

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

    section[data-testid="stMain"] .stNumberInput input::-webkit-outer-spin-button,
    section[data-testid="stMain"] .stNumberInput input::-webkit-inner-spin-button {
        -webkit-appearance: none !important;
        margin: 0 !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
    }

    section[data-testid="stMain"] .stNumberInput input[type="number"] {
        -moz-appearance: textfield !important;
    }
    
    
    /* ========== SELECTBOX - TARGET CORRECT WRAPPER ========== */
    
    /* The OUTER wrapper - this is what we want to style */
    section[data-testid="stMain"] div.stSelectbox > div > div:first-child {
        background: rgba(10, 14, 39, 0.95) !important;
        border: 3px solid rgba(13, 110, 253, 0.6) !important;
        border-radius: 12px !important;
        min-height: 48px !important;
        padding: 0 18px !important;
        box-shadow: 
            0 0 25px rgba(13, 110, 253, 0.3) !important,
            inset 0 0 20px rgba(13, 110, 253, 0.08) !important;
        display: flex !important;
        align-items: center !important;
        transition: all 0.3s ease !important;
        overflow: hidden !important;
    }
    
    @keyframes selectCyanGlow {
        0%, 100% { 
            border-color: #0d6efd !important;
            box-shadow: 
                0 0 45px rgba(13, 110, 253, 0.65),
                0 0 35px rgba(138, 43, 226, 0.45),
                inset 0 0 40px rgba(13, 110, 253, 0.18) !important;
        }
        50% { 
            border-color: #8a2be2 !important;
            box-shadow: 
                0 0 55px rgba(138, 43, 226, 0.75),
                0 0 45px rgba(13, 110, 253, 0.55),
                inset 0 0 50px rgba(138, 43, 226, 0.25) !important;
        }
    }
    
    /* Hover */
    section[data-testid="stMain"] div.stSelectbox > div > div:first-child:hover {
        border-color: rgba(13, 110, 253, 0.85) !important;
        box-shadow: 
            0 0 35px rgba(13, 110, 253, 0.5) !important,
            inset 0 0 25px rgba(13, 110, 253, 0.12) !important;
    }
    
    /* CRITICAL: Remove the brackets { } by hiding inner baseweb select borders */
    section[data-testid="stMain"] div.stSelectbox [data-baseweb="select"],
    section[data-testid="stMain"] div.stSelectbox [data-baseweb="select"] *,
    section[data-testid="stMain"] div.stSelectbox [role="button"],
    section[data-testid="stMain"] div.stSelectbox [role="button"] * {
        border: none !important;
        border-left: none !important;
        border-right: none !important;
        border-top: none !important;
        border-bottom: none !important;
        border-width: 0 !important;
        border-style: none !important;
        background: transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }
    
    /* Force transparent on EVERYTHING inside */
    section[data-testid="stMain"] div.stSelectbox div[class*="css-"],
    section[data-testid="stMain"] div.stSelectbox div[class^="st-"] {
        border: none !important;
        background: transparent !important;
    }
    
    /* Text */
    section[data-testid="stMain"] div.stSelectbox span {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
    }
    
    /* Arrow */
    section[data-testid="stMain"] div.stSelectbox svg {
        fill: #0d6efd !important;
        width: 24px !important;
        height: 24px !important;
        filter: drop-shadow(0 4px 18px rgba(13,110,253,0.8)) !important;
    }
    
    section[data-testid="stMain"] div.stSelectbox:hover svg {
        fill: #0d6efd !important;
        filter: drop-shadow(0 5px 22px rgba(13,110,253,0.9)) !important;
    }
    
    /* Dropdown Menu */
    div[data-baseweb="menu"] {
        background: linear-gradient(180deg, rgba(10,14,39,0.98), rgba(10,14,39,0.96)) !important;
        border: 2px solid rgba(13, 110, 253, 0.3) !important;
        border-radius: 10px !important;
        box-shadow: 0 0 25px rgba(13, 110, 253, 0.22), inset 0 2px 8px rgba(13,110,253,0.02) !important;
        backdrop-filter: blur(2px);
        margin-top: 5px;
    }
    
    div[data-baseweb="menu"] li {
        color: #e2e8f0 !important;
        padding: 0.75vh 1.1vw !important;
        font-weight: 500 !important;
        font-size: clamp(0.9rem, 0.95vw, 1rem) !important;
        transition: all 0.15s ease !important;
        border-bottom: 1px solid rgba(13, 110, 253, 0.05) !important;
        margin: 0.25vh 0.5vw !important;
        border-radius: 5px !important;
    }
    
    div[data-baseweb="menu"] li:last-child {
        border-bottom: none !important;
    }
    
    div[data-baseweb="menu"] li:hover {
        background: linear-gradient(90deg, rgba(13, 110, 253, 0.2), rgba(138, 43, 226, 0.1)) !important;
        box-shadow: inset 0 0 12px rgba(13, 110, 253, 0.05) !important;
        color: #ffffff !important;
        transform: translateX(2px);
    }
    
    /* Slider Styling - responsive */
    section[data-testid="stMain"] .stSlider > div > div > div {
        background: rgba(13, 110, 253, 0.13) !important;
        height: clamp(7px, 0.8vh, 8px) !important;
        border-radius: 8px !important;
        box-shadow: 0 0 10px rgba(13, 110, 253, 0.15) !important;
    }
    
    section[data-testid="stMain"] .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #0d6efd, #8a2be2) !important;
        box-shadow: 0 0 15px rgba(13, 110, 253, 0.3) !important;
    }
    
    section[data-testid="stMain"] .stSlider [role="slider"] {
        background: #fff !important;
        width: clamp(20px, 2vw, 22px) !important;
        height: clamp(20px, 2vw, 22px) !important;
        border: 3px solid #0d6efd !important;
        box-shadow: 0 0 18px rgba(13, 110, 253, 0.45) !important;
        animation: sliderGlow 2s ease-in-out infinite;
    }
    
    @keyframes sliderGlow {
        0%, 100% { 
            box-shadow: 0 0 18px rgba(13, 110, 253, 0.45);
        }
        50% { 
            box-shadow: 0 0 26px rgba(138, 43, 226, 0.65);
        }
    }
    
    /* Time Badge - responsive */
    .time-badge {
        background: rgba(13, 110, 253, 0.11);
        border: 2px solid rgba(13, 110, 253, 0.28);
        border-radius: 8px;
        padding: 0.8vh 1.2vw;
        text-align: center;
        margin-top: 0.6vh;
        font-weight: 700;
        font-size: clamp(1.2rem, 1.3vw, 1.4rem);
        box-shadow: 0 0 15px rgba(13, 110, 253, 0.16);
        animation: badgeGlow 3s ease-in-out infinite;
    }
    
    @keyframes badgeGlow {
        0%, 100% { 
            box-shadow: 0 0 15px rgba(13, 110, 253, 0.16);
        }
        50% { 
            box-shadow: 0 0 22px rgba(138, 43, 226, 0.3);
        }
    }
    
    section[data-testid="stMain"] .stSlider > label {
        font-size: clamp(1rem, 1.1vw, 1.15rem) !important;
        font-weight: 600 !important;
    }
    
    section[data-testid="stMain"] .stSlider span {
        font-size: clamp(0.9rem, 0.95vw, 1rem) !important;
        font-weight: 600 !important;
    }
    
    /* Ratio Display Card - responsive */
    .ratio-display {
        background: linear-gradient(135deg, rgba(13, 110, 253, 0.11) 0%, rgba(138, 43, 226, 0.11) 100%);
        border: 2px solid rgba(13, 110, 253, 0.28);
        border-radius: 15px;
        padding: 1.6vh 1.2vw;
        margin: 1.6vh 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 30px rgba(13, 110, 253, 0.16);
        animation: cardGlow 4s ease-in-out infinite;
    }
    
    @keyframes cardGlow {
        0%, 100% { 
            box-shadow: 0 0 30px rgba(13, 110, 253, 0.16);
            border-color: rgba(13, 110, 253, 0.28);
        }
        50% { 
            box-shadow: 0 0 40px rgba(138, 43, 226, 0.32);
            border-color: rgba(138, 43, 226, 0.38);
        }
    }
    
    .ratio-display::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .ratio-label {
        color: #8892b0;
        font-size: clamp(0.85rem, 0.9vw, 0.95rem);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.6vh;
    }
    
    .ratio-value {
        font-size: clamp(2.5rem, 2.8vw, 3rem);
        font-weight: 800;
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        text-shadow: 0 0 22px rgba(13, 110, 253, 0.22);
    }
    
    /* Warning Box - responsive */
    .warning-box {
        background: rgba(239, 68, 68, 0.11);
        border: 2px solid rgba(239, 68, 68, 0.28);
        border-radius: 10px;
        padding: 0.85vh 1.1vw;
        color: #f87171;
        font-size: clamp(0.9rem, 0.95vw, 1rem);
        font-weight: 600;
        margin: 1.5vh 0;
        display: flex;
        align-items: center;
        gap: 0.7vw;
        box-shadow: 0 0 18px rgba(239, 68, 68, 0.16);
        animation: warningPulse 2s ease-in-out infinite;
    }
    
    @keyframes warningPulse {
        0%, 100% { 
            box-shadow: 0 0 18px rgba(239, 68, 68, 0.16);
        }
        50% { 
            box-shadow: 0 0 26px rgba(239, 68, 68, 0.32);
        }
    }
    
    /* Button Styling - responsive */
    section[data-testid="stMain"] .stButton > button {
        background: linear-gradient(135deg, #0d6efd 0%, #8a2be2 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        font-size: clamp(1.1rem, 1.15vw, 1.2rem) !important;
        padding: 1vh 2.2vw !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 8px 26px rgba(13, 110, 253, 0.32) !important;
        text-transform: uppercase !important;
        letter-spacing: 3.5px !important;
        transition: all 0.3s ease !important;
        min-height: clamp(48px, 5vh, 52px) !important;
        animation: buttonGlow 3s ease-in-out infinite;
        line-height: 1.1 !important;
    }
    
    section[data-testid="stMain"] .stButton > button * {
        font-size: clamp(1.1rem, 1.15vw, 1.2rem) !important;
        font-weight: 700 !important;
        line-height: 1.1 !important;
    }
    
    @keyframes buttonGlow {
        0%, 100% { 
            box-shadow: 0 8px 26px rgba(13, 110, 253, 0.32);
        }
        50% { 
            box-shadow: 0 11px 36px rgba(138, 43, 226, 0.5);
        }
    }
    
    section[data-testid="stMain"] .stButton > button:hover:not(:disabled) {
        transform: translateY(-2px) !important;
        box-shadow: 0 13px 40px rgba(13, 110, 253, 0.55) !important;
    }
    
    section[data-testid="stMain"] .stButton > button:disabled {
        background: linear-gradient(135deg, #374151 0%, #4b5563 100%) !important;
        opacity: 0.6 !important;
        cursor: not-allowed !important;
        animation: none !important;
    }
    
    .row-widget.stHorizontal {
        gap: 1.5vw !important;
    }
    
    /* Page heading styles - responsive with MORE top margin for spacing */
    .page-heading {
        font-size: clamp(1.6rem, 1.8vw, 1.9rem);
        font-weight: 700;
        text-align: center;
        margin-top: 4vh;  /* Increased from 1vh to 4vh */
        margin-bottom: 2vh;  /* Increased from 1.5vh to 2vh */
        letter-spacing: 0.25px;
        color: #ffffff;
        position: relative;
        display: inline-block;
        width: 100%;
    }
    .page-heading::after {
        content: '';
        position: absolute;
        bottom: -6px;
        left: 50%;
        transform: translateX(-50%);
        width: clamp(90px, 8vw, 110px);
        height: 2px;
        background: linear-gradient(90deg, #0d6efd, #8a2be2);
        border-radius: 2px;
        box-shadow: 0 4px 12px rgba(13, 110, 253, 0.16);
    }
    .page-subtext {
        text-align: center;
        color: #9fb0c8;
        font-size: clamp(0.75rem, 0.8vw, 0.85rem);
        margin-bottom: 1vh;
        font-weight: 600;
    }
    /* Full-page overlay loader - responsive */
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
        width: min(680px, 85vw);
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.04);
        border-radius: 14px;
        padding: 2vh 2vw;
        box-shadow: 0 12px 45px rgba(2,6,23,0.45), 0 5px 26px rgba(13,110,253,0.04);
        display: flex; flex-direction: column; align-items: center; gap: 0.7vh;
    }

    .tg-loader-wrap { display:flex; align-items:center; gap:1vw; }

    .tg-loader {
        width: clamp(64px, 6vw, 72px); 
        height: clamp(64px, 6vw, 72px); 
        border-radius: 50%;
        background: conic-gradient(from 0deg, #0d6efd, #8a2be2, #6b46c1);
        display:flex; align-items:center; justify-content:center; position: relative;
        box-shadow: 0 7px 32px rgba(13,110,253,0.18), inset 0 -4px 13px rgba(0,0,0,0.2);
        animation: tg-spin 1.8s linear infinite;
    }

    .tg-loader-inner { 
        width: clamp(44px, 4vw, 48px); 
        height: clamp(44px, 4vw, 48px); 
        border-radius:50%; 
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02)); 
        display:flex; align-items:center; justify-content:center; 
        font-size: clamp(20px, 2.2vw, 25px); 
    }
    @keyframes tg-spin { to { transform: rotate(360deg); } }

    .tg-title { 
        font-size: clamp(1.05rem, 1.15vw, 1.2rem); 
        font-weight: 800; 
        margin: 0.4vh 0 0.12vh 0; 
        letter-spacing: 0.45px; 
        background: linear-gradient(90deg,#fff,#cbd5e1); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
    }
    .tg-sub { 
        color: #cbd5e1; 
        font-size: clamp(0.8rem, 0.85vw, 0.85rem); 
        margin: 0; 
    }

    .tg-progress { 
        margin-top: 0.7vh; 
        width: 78%; 
        height: clamp(8px, 0.9vh, 9px); 
        background: rgba(255,255,255,0.03); 
        border-radius: 7px; 
        overflow: hidden; 
    }
    .tg-progress-bar { 
        height: 100%; 
        width: 0%; 
        background: linear-gradient(90deg,#0d6efd,#8a2be2); 
        border-radius: 7px; 
        box-shadow: 0 5px 18px rgba(13,110,253,0.18); 
        animation: tg-progress-anim 4s linear forwards; 
    }
    @keyframes tg-progress-anim { from { width: 0%; } to { width: 100%; } }

    .tg-dots{ margin-top: 0.55vh; }
    .tg-dots span{ 
        display:inline-block; 
        width: clamp(6px, 0.6vw, 7px); 
        height: clamp(6px, 0.6vw, 7px); 
        margin: 0 0.3vw; 
        background: #fff; 
        border-radius:50%; 
        opacity:0.13; 
        box-shadow:0 4px 13px rgba(13,110,253,0.04); 
        animation: tg-dots 1s infinite; 
    }
    .tg-dots span:nth-child(1){ animation-delay: 0s } 
    .tg-dots span:nth-child(2){ animation-delay: 0.14s } 
    .tg-dots span:nth-child(3){ animation-delay: 0.28s }
    @keyframes tg-dots{ 
        0%{opacity:0.13; transform: translateY(0)} 
        50%{opacity:1; transform: translateY(-6px)} 
        100%{opacity:0.13; transform: translateY(0)} 
    }

</style>
""", unsafe_allow_html=True)

# Page Title - with more top margin
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
        predict_disabled = True
        st.markdown(
            '<div class="warning-box">⚠️ Transaction amount cannot exceed sender balance!</div>',
            unsafe_allow_html=True
        )
    else:
        predict_disabled = False
        st.markdown(f"""
        <div class="ratio-display">
            <div class="ratio-label">💸 Amount to Sender Balance Ratio</div>
            <div class="ratio-value">{amount_to_sender_balance_ratio:.4f}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    # sender_init_balance == 0 → ratio is 0 and prediction disabled
    amount_to_sender_balance_ratio = 0.0
    predict_disabled = True

    st.markdown(
        '<div class="warning-box">⚠️ Sender initial balance is 0 — prediction disabled!</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="ratio-display">
        <div class="ratio-label">💸 Amount to Sender Balance Ratio</div>
        <div class="ratio-value">0.0000</div>
    </div>
    """, unsafe_allow_html=True)


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

st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)

# Validation logic
error_message = ""

# Check if transaction amount is 0
if transaction_amount == 0:
    predict_disabled = True
    error_message = "⚠️ Transaction amount cannot be $0.00. Please enter a valid amount."
# Check if transaction amount exceeds sender balance
elif sender_init_balance > 0 and transaction_amount > sender_init_balance:
    predict_disabled = True
    error_message = "⚠️ Transaction amount cannot exceed sender balance!"

# Display error message if any
if error_message:
    st.markdown(f'''
    <div style="
        background: linear-gradient(135deg, rgba(220,38,38,0.12), rgba(239,68,68,0.08));
        border: 2px solid rgba(220,38,38,0.4);
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 20px;
        color: #fca5a5;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: center;
        box-shadow: 0 4px 16px rgba(220,38,38,0.2);
    ">
        {error_message}
    </div>
    ''', unsafe_allow_html=True)

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

    # ✅ ADD RATIO TO RESULT BEFORE STORING
    if result is not None:
        result['amount_to_sender_balance_ratio'] = amount_to_sender_balance_ratio

    st.session_state.prediction_result = result
    # remove overlay before switching
    overlay_placeholder.empty()
    st.switch_page("pages/03_Results.py")
