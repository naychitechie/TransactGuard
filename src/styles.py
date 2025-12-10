"""Styling helpers for TransactGuard Streamlit app."""

def _get_streamlit():
    try:
        import streamlit as st
        return st
    except Exception:
        class _SidebarStub:
            def __enter__(self): return self
            def __exit__(self, exc_type, exc, tb): return False

        class _StStub:
            def __init__(self):
                self.sidebar = _SidebarStub()
            def markdown(self, *args, **kwargs): pass
            def button(self, *args, **kwargs): return False
            def switch_page(self, *args, **kwargs): pass
            @property
            def session_state(self):
                class SessionState:
                    pass
                return SessionState()

        return _StStub()


def apply_dark_theme():
    """Inject global dark theme CSS and a sticky top banner across pages."""
    st = _get_streamlit()
    
    dark_theme_css = """
    <style>
    :root {
        /* Palette tokens (user-provided) */
        --bg-page: #07041A;
        --bg-card: #07061A;

        --text-heading: #F9FAFB;   /* large section headings */
        --text-title:   #E5E7EB;   /* card titles */
        --text-body:    #9CA3AF;   /* descriptions and small text */

        --nav-link:        #C7BBF8;   /* default nav link text (light lavender) */
        --nav-link-hover:  #E5E7EB;   /* hover state (lighter) */
        --nav-link-active: #A855FF;   /* active/selected link */
        --accent-secondary: #7dd3fc;  /* added for brand gradient fallback */

        /* Backwards-compatible tokens (map to new ones) */
        --bg-elevated: var(--bg-card);
        --text-primary: var(--text-heading);
        --text-secondary: var(--text-title);
        --text-muted: var(--text-body);
        --text-accent: var(--nav-link-active);

        --border-subtle: #111827;
        --nav-height: 74px;
        --font-stack: system-ui, -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", sans-serif;
    }

    MainMenu { visibility: hidden }
    footer { visibility: hidden !important; }
    [data-testid="stToolbar"] { visibility: hidden !important; }

    /* Hide Streamlit native sidebar/header and all toggle buttons */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] nav,
    [data-testid="stSidebar"] [role="navigation"],
    [data-testid="stSidebar"] ul { 
        display: none !important; 
        visibility: hidden !important; 
    }
    /* Hide any collapse/expand floating toggles that Streamlit injects */
    [data-testid="collapsedControl"],
    button[title*="collapse"],
    button[aria-label*="collapse"],
    button[aria-label*="Collapse"],
    button[aria-label*="expand"],
    button[aria-label*="Expand"],
    button[aria-label*="Show"],
    button[aria-label*="Hide"],
    div[style*="position: fixed"][style*="left: 0"][style*="top: 0"] button {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }
    /* Extra catch-all for new Streamlit sidebar toggles */
    [data-testid="collapsedControl"] > button,
    [data-testid="stSidebarCollapseButton"],
    button[aria-label*="sidebar"],
    button[title*="sidebar"],
    button[aria-label*="Sidebar"],
    button[title*="Sidebar"],
    button[aria-label*="Menu"],
    button[title*="Menu"],
    button[aria-label^="Open"],
    button[aria-label^="Close"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }

    /* Force-hide any remaining sidebar toggle buttons (purple pill) */
    [data-testid="collapsedControl"],
    [data-testid="collapsedControl"] *,
    [data-testid="stSidebarButton"],
    [data-testid="stSidebarButton"] *,
    button[aria-label*="sidebar"],
    button[aria-label*="Sidebar"],
    button[title*="sidebar"],
    button[title*="Sidebar"],
    button[aria-label*="menu"],
    button[aria-label*="Menu"],
    button[aria-label*="navigation"],
    button[title*="navigation"],
    div[style*="position: fixed"][style*="left: 0"][style*="top: 0"] button {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }
    /* Hide common Streamlit collapse classes */
    .css-1v3fvcr, .css-1q8dd3e, .st-emotion-cache-1dj3f8j, .st-emotion-cache-1v0mbdj {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important; height: 0 !important; padding: 0 !important; margin: 0 !important;
        pointer-events: none !important; overflow: hidden !important;
    }
    
    /* Hide ONLY Streamlit native header / toolbar buttons so we don't hide app action buttons */
    [data-testid="stHeader"] button,
    [data-testid="stHeader"] [class*="st-emotion"] button,
    header[data-testid="stHeader"] button,
    header nav > button,
    div[style*="position: fixed"][style*="top: 0"][style*="left: 0"] > button {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }
    
    /* Hide top-left area where toggle button typically lives */
    .st-emotion-cache-1wmy9hs,
    .st-emotion-cache-hxt3ql,
    div[style*="position: fixed"][style*="top: 0"][style*="left: 0"] > button {
        display: none !important;
        visibility: hidden !important;
    }
    
    header, [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Apply global background and typography */
    [data-testid="stAppViewContainer"] { background: var(--bg-page) !important; }
    main, body, .appview-container, .reportview-container { background: var(--bg-page) !important; }
    body {
        min-height: 100vh;
        margin: 0;
        padding: 0;
        font-family: var(--font-stack);
        color: var(--text-secondary);
        background: #07041A;
    }

    /* Ensure headings and navigation use the same sans-serif stack */
    h1, h2, h3, h4 { font-family: var(--font-stack); color: var(--text-heading); }
    nav, a, button { font-family: var(--font-stack); }

    /* Section headings (explicit) */
    .section-title { color: var(--text-heading) !important; }

    /* Card title and body mappings */
    .card h3 { color: var(--text-title) !important; }
    .card p, .card small { color: var(--text-body) !important; }
    .card { background-color: var(--bg-card); }

    /* top navigation */
    .top-nav {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: var(--nav-height);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 28px;
        background: rgba(5, 5, 21, 0.7);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        z-index: 999999; /* ensure nav is above any stray Streamlit controls */
    }
    /* Hide any rogue button that may sit on top of the brand area */
    .top-nav button,
    .top-nav [role="button"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }
    .nav-left { display: flex; align-items: center; gap: 10px; color: var(--text-accent); font-weight: 800; font-size: 22px; text-decoration: none; flex: 1; }
    .nav-center { display: flex; gap: 8px; align-items: center; justify-content: center; flex: 1; }
    .nav-right { display: flex; align-items: center; gap: 10px; flex: 1; justify-content: flex-end; }
    .nav-link {
        color: var(--nav-link) !important;
        text-decoration: none;
        font-size: 16px;
        font-weight: 700;
        padding: 8px 12px;
        border-radius: 10px;
        transition: all 0.18s ease;
    }
    /* Ensure no underlines on anchors and nav links across the app */
    a, .nav-link { text-decoration: none !important; }
    .nav-link:hover { color: var(--nav-link-hover); background: rgba(168,85,255,0.08); text-decoration: none !important; }
    .nav-link.active { color: var(--nav-link-active); border: 1px solid rgba(168,85,255,0.16); background: rgba(168,85,255,0.12); box-shadow: 0 8px 24px rgba(24, 8, 53, 0.45); text-decoration: none !important; }
    .nav-spacer { display: none; } /* to balance space on right for alignment */

    /* Animated brand + shield */
    .nav-left { display: flex; align-items: center; gap: 12px; color: var(--text-accent); font-weight: 800; font-size: 20px; text-decoration: none !important; flex: 1; }
    .nav-left:hover { text-decoration: none !important; }
    .nav-cta {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #9487FF, #59e6ff, #b48dff);
        background-size: 220% 220%;
        color: #0b0a1c !important;
        border: 1px solid rgba(199, 187, 248, 0.45);
        padding: 11px 18px;
        border-radius: 14px;
        font-weight: 800;
        text-decoration: none !important;
        box-shadow: 0 12px 44px rgba(148,135,255,0.6), 0 0 40px rgba(148,135,255,0.55);
        animation: sheen 6s ease-in-out infinite, pulseGlow 2.2s ease-in-out infinite;
        isolation: isolate;
        color: #0b0a1c !important;
    }
    .nav-cta-text {
        position: relative;
        z-index: 3;
    }
    /* Animated paint stroke around the button */
    .nav-cta::before {
        content: "";
        position: absolute;
        inset: -2px;
        border-radius: 16px;
        background: conic-gradient(from 0deg, #9487FF, #59e6ff, #b48dff, #9487FF);
        animation: paintSweep 2.8s linear infinite;
        z-index: 1;
        -webkit-mask:
          linear-gradient(#000 0 0) content-box,
          linear-gradient(#000 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        padding: 3px;
    }
    .nav-cta::after {
        content: "";
        position: absolute;
        inset: 2px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0.08));
        z-index: 2;
    }
    /* Hide old sparkles */
    .nav-cta .sparkle { display: none !important; }

    .nav-cta:hover { filter: brightness(1.06); transform: translateY(-1px); }
    @keyframes sheen {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 12px 44px rgba(148,135,255,0.6), 0 0 40px rgba(148,135,255,0.55); }
        50% { box-shadow: 0 16px 56px rgba(148,135,255,0.7), 0 0 52px rgba(148,135,255,0.65); }
    }
    @keyframes paintSweep {
        to { transform: rotate(360deg); }
    }
    .shield-svg { width: 38px; height: 38px; display: inline-block; transform-origin: center; filter: drop-shadow(0 10px 30px rgba(168,85,255,0.18)); animation: float 2.8s ease-in-out infinite, pulse 1.6s ease-in-out infinite; }
    @keyframes float { 0% { transform: translateY(0px) rotateZ(0deg); } 25% { transform: translateY(-10px) rotateZ(2deg); } 50% { transform: translateY(-2px) rotateZ(-2deg); } 75% { transform: translateY(-10px) rotateZ(2deg); } 100% { transform: translateY(0px) rotateZ(0deg); } }
    @keyframes pulse { 0% { filter: drop-shadow(0 10px 30px rgba(168,85,255,0.18)); } 50% { filter: drop-shadow(0 15px 50px rgba(168,85,255,0.45)); } 100% { filter: drop-shadow(0 10px 30px rgba(168,85,255,0.18)); } }
    .brand-text { 
        display: inline-block; 
        font-weight: 900; 
        letter-spacing: -0.5px; 
        background: linear-gradient(90deg, var(--text-accent), #ff66ff 40%, var(--accent-secondary)); 
        background-size: 200% 100%; 
        -webkit-background-clip: text; 
        background-clip: text; 
        color: var(--text-accent); 
        -webkit-text-fill-color: transparent; 
        animation: hueShift 4s linear infinite, neonPulse 1.8s ease-in-out infinite; 
        text-decoration: none !important; 
        z-index: 200010;
    }
    @keyframes hueShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes neonPulse { 0% { text-shadow: 0 0 10px rgba(168,85,255,0.2); } 50% { text-shadow: 0 0 28px rgba(168,85,255,0.8), 0 8px 40px rgba(99,102,241,0.35), 0 0 60px rgba(255,102,255,0.25); } 100% { text-shadow: 0 0 10px rgba(168,85,255,0.2); } }

    /* pad main content below nav */
    [data-testid="stAppViewContainer"] > .main {
        padding-top: calc(var(--nav-height) + 28px) !important;
        padding-left: 32px !important;
        padding-right: 32px !important;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Hero section with neon arch background */
    .hero-section-wrapper {
        position: relative;
        margin: 0 auto 32px auto;
        max-width: 1200px;
        width: 100%;
        padding: 0 32px;
    }

    .hero-section-wrapper img {
        width: 100%;
        height: auto;
        display: block;
    }

    .hero-text-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding: 56px 32px;
        text-align: center;
        z-index: 10;
        background: rgba(5, 3, 22, 0.08); /* lighter overlay so arch shines through */
        max-width: 1200px;
        margin: 0 auto;
    }

    .hero-bg { object-fit: cover; width: 100%; height: 360px; display: block; }
    .hero-text-overlay .hero-title { text-shadow: 0 8px 30px rgba(2,2,8,0.7), 0 2px 8px rgba(168,85,255,0.08); }
    .hero-text-overlay p { text-shadow: 0 6px 18px rgba(2,2,8,0.6); }

    .hero-section {
        display: none;
    }

    /* Bright glowing button styles (less dark, stronger neon glow) */
    :root {
        --btn-glow-top: #9487FF;
        --btn-glow-bottom: #7f73e6;
        --btn-border-strong: rgba(148, 135, 255, 0.35);
        --btn-text-glow: #ffffff;
        --btn-neon-glow: rgba(148,135,255,0.32);
    }

    /* Inputs and selects */
    input, select, textarea, .stTextInput input, .stNumberInput input {
        background: rgba(10, 14, 40, 0.82) !important;
        color: #e8ecff !important;
        border: 1px solid rgba(86, 134, 255, 0.5) !important;
        border-radius: 14px !important;
        padding: 12px 14px !important;
        box-shadow:
            inset 0 0 0 1px rgba(86, 134, 255, 0.2),
            0 0 0 1px rgba(86, 134, 255, 0.35),
            0 14px 28px rgba(0,0,0,0.45),
            0 0 24px rgba(86, 134, 255, 0.28) !important;
    }
    input:focus, select:focus, textarea:focus, .stTextInput input:focus, .stNumberInput input:focus {
        outline: none !important;
        border-color: rgba(120, 170, 255, 0.85) !important;
        box-shadow:
            inset 0 0 0 1px rgba(120, 170, 255, 0.4),
            0 0 0 1px rgba(120, 170, 255, 0.8),
            0 14px 28px rgba(0,0,0,0.5),
            0 0 28px rgba(120, 170, 255, 0.36) !important;
    }

    /* Apply to Streamlit buttons and common button inputs */
    .stButton > button, button, input[type="button"], input[type="submit"], .css-1emrehy button {
        background: linear-gradient(180deg, var(--btn-glow-top), var(--btn-glow-bottom)) !important;
        border: 1px solid var(--btn-border-strong) !important;
        color: var(--btn-text-glow) !important;
        padding: 10px 24px !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 0.3px !important;
        text-shadow: 0 1px 0 rgba(0,0,0,0.45) !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.03), 0 10px 32px rgba(6,4,18,0.45), 0 0 40px var(--btn-neon-glow) !important;
        transition: transform 160ms ease, box-shadow 220ms ease, background 160ms ease !important;
        -webkit-appearance: none !important;
        cursor: pointer !important;
        backdrop-filter: blur(2px) !important;
    }

    /* Hover: stronger glow, slight lift */
    .stButton > button:hover, button:hover, input[type="button"]:hover, input[type="submit"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.06), 0 28px 68px rgba(148,135,255,0.32), 0 0 72px rgba(148,135,255,0.38) !important;
        background: linear-gradient(180deg, #a39bff 0%, #8579f0 100%) !important;
    }

    /* Active / pressed state */
    .stButton > button:active, button:active, input[type="button"]:active, input[type="submit"]:active {
        transform: translateY(0px) scale(0.995) !important;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.5), 0 8px 22px rgba(6,4,18,0.5) !important;
    }

    /* Focus: clear neon halo */
    .stButton > button:focus, button:focus, input[type="button"]:focus, input[type="submit"]:focus {
        outline: none !important;
        box-shadow: 0 12px 56px rgba(148,135,255,0.32), 0 0 56px rgba(148,135,255,0.38) !important;
    }


    /* (No global overrides here) */


    .hero-section::before {
        display: none;
    }

    .hero-section > * {
        position: relative;
        z-index: 1;
    }

    .card { background-color: var(--bg-elevated); border: 1px solid var(--border-subtle); padding: 14px; border-radius: 10px; margin-bottom: 14px; color: var(--text-secondary) !important; }
    .hero-title { font-size: 56px; margin: 16px 0 8px 0; color: var(--text-primary) !important; opacity: 1 !important; font-weight: 900; letter-spacing: -1px; }

    </style>

    <div class="top-nav">
      <a class="nav-left" href="/Home" data-page="Home" style="cursor: pointer;" target="_self">
        <svg class="shield-svg" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="g1" x1="0%" x2="100%" y1="0%" y2="100%">
              <stop offset="0%" stop-color="#a855ff" />
              <stop offset="50%" stop-color="#ff66ff" />
              <stop offset="100%" stop-color="#6366f1" />
            </linearGradient>
            <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>
          </defs>
          <g filter="url(#softGlow)">
            <path d="M32 4 L12 12 v14 c0 18 10 30 20 34 10-4 20-16 20-34V12L32 4z" fill="url(#g1)" opacity="0.98" />
            <path d="M32 10 L20 16 v10 c0 14 6 24 12 28 6-4 12-14 12-28V16L32 10z" fill="rgba(255,255,255,0.06)" />
          </g>
        </svg>
        <span class="brand-text">TransactGuard</span>
      </a>
      <div class="nav-center">
        <a class="nav-link" href="/Data" data-page="Data" style="cursor: pointer;" target="_self">Data</a>
        <a class="nav-link" href="/Results" data-page="Results" style="cursor: pointer;" target="_self">Results</a>
        <a class="nav-link" href="/About" data-page="About" style="cursor: pointer;" target="_self">About</a>
      </div>
      <div class="nav-right">
        <a class="nav-cta" href="/Predict" data-page="Predict" style="cursor: pointer;" target="_self">
          <span class="sparkle"></span>
          <span class="sparkle"></span>
          <span class="sparkle"></span>
          <span class="sparkle"></span>
          <span class="sparkle"></span>
          <span class="sparkle"></span>
          <span class="nav-cta-text">Predict</span>
        </a>
      </div>
    </div>

    <script>
    // Aggressively remove any button/div/anchor in the top-left area (Streamlit sidebar toggle)
    function nukeTopLeftControls() {
        const targets = document.querySelectorAll('button, div, a');
        targets.forEach(el => {
            try {
                if (el.classList.contains('nav-left') || el.classList.contains('nav-link') || el.classList.contains('nav-cta') || el.getAttribute('data-page')) return;
                const rect = el.getBoundingClientRect();
                if (!rect || rect.width === 0 || rect.height === 0) return;
                if (rect.left > 260 || rect.top > 220) return;
                if (rect.width > 300 || rect.height > 200) return;
                el.style.setProperty('display', 'none', 'important');
                el.style.setProperty('visibility', 'hidden', 'important');
                el.style.setProperty('width', '0px', 'important');
                el.style.setProperty('height', '0px', 'important');
                el.style.setProperty('padding', '0px', 'important');
                el.style.setProperty('margin', '0px', 'important');
                el.style.setProperty('pointer-events', 'none', 'important');
                el.setAttribute('data-removed-by', 'top-left-nuke');
            } catch (e) { /* ignore */ }
        });
    }

    // Run on load and periodically to catch dynamically injected elements
    window.addEventListener('load', nukeTopLeftControls);
    document.addEventListener('DOMContentLoaded', nukeTopLeftControls);
    setInterval(nukeTopLeftControls, 400);
    
    // Handle top navigation bar (use Streamlit page slugs; rely on anchors)
    document.addEventListener('DOMContentLoaded', function() {
        const navLinks = document.querySelectorAll('.nav-left, .nav-link, .nav-cta');
        navLinks.forEach(link => { try { link.target = '_self'; } catch (e) {} });

        // Update active state based on path slug
        const path = window.location.pathname.replace(/^\\/+/, ''); // remove leading slash
        const slug = path || 'Home';
        navLinks.forEach(link => {
            if ((link.getAttribute('data-page') || '').toLowerCase() === slug.toLowerCase()) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });

        // Remove any element overlapping the brand area (e.g., leftover sidebar toggle)
        function hideObstructions() {
            const brand = document.querySelector('.nav-left');
            const bRect = brand ? brand.getBoundingClientRect() : null;
            const candidates = document.querySelectorAll('button, a, div[role="button"]');
            candidates.forEach(el => {
                try {
                    if (el.closest('.top-nav')) return; // keep our nav intact
                    if (el.classList.contains('nav-left') || el.classList.contains('nav-link') || el.classList.contains('nav-cta') || el.getAttribute('data-page')) return;
                    const r = el.getBoundingClientRect();
                    if (!r || r.width === 0 || r.height === 0) return;
                    const inTopLeft = r.left < 400 && r.top < 400; // aggressive top-left removal
                    let overlaps = false;
                    let nearBrand = false;
                    if (bRect) {
                        overlaps = !(r.right < bRect.left || r.left > bRect.right || r.bottom < bRect.top || r.top > bRect.bottom);
                        nearBrand = r.top < bRect.bottom + 80 && r.left < bRect.right + 80;
                    }
                    if (inTopLeft || overlaps || nearBrand) {
                        el.style.setProperty('display', 'none', 'important');
                        el.style.setProperty('visibility', 'hidden', 'important');
                        el.style.setProperty('width', '0px', 'important');
                        el.style.setProperty('height', '0px', 'important');
                        el.style.setProperty('padding', '0px', 'important');
                        el.style.setProperty('margin', '0px', 'important');
                        el.style.setProperty('pointer-events', 'none', 'important');
                        el.setAttribute('data-removed-by', 'brand-protect');
                    }
                } catch (e) { /* ignore */ }
            });
        }
        hideObstructions();
        const observer = new MutationObserver(hideObstructions);
        observer.observe(document.body, { childList: true, subtree: true });
    });
    </script>
    """
    st.markdown(dark_theme_css, unsafe_allow_html=True)


def render_sidebar():
    """Render navigation in the Streamlit sidebar using native page switching."""
    st = _get_streamlit()
    
    with st.sidebar:
        st.markdown("""
        <style>
        .nav-button-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Create navigation buttons that use Streamlit's native page switching
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("Home", use_container_width=True, key="nav_home"):
                st.switch_page("pages/01_Home.py")

        with col2:
            if st.button("Predict", use_container_width=True, key="nav_predict"):
                st.switch_page("pages/02_Predict.py")

        with col3:
            if st.button("Results", use_container_width=True, key="nav_results"):
                st.switch_page("pages/03_Results.py")

        with col4:
            if st.button("Data", use_container_width=True, key="nav_data"):
                st.switch_page("pages/04_Data.py")
        
        st.markdown("---")
        
        if st.button("About", use_container_width=True, key="nav_about"):
            st.switch_page("pages/05_About.py")
