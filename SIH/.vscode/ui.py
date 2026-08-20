"""
Nagar Sanchalak — single-file Streamlit app
Login: username = admin, password = admin

Run with:
    pip install streamlit
    streamlit run nagar_sanchalak_app.py
"""

import streamlit as st
import time

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Nagar Sanchalak",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Hardcoded credentials
# ---------------------------------------------------------------------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

# ---------------------------------------------------------------------------
# Dummy civic data (stand-in for what the real multi-agent backend would send)
# ---------------------------------------------------------------------------
ISSUES = [
    {
        "id": "NS-4471",
        "category": "Pothole",
        "icon": "🕳️",
        "location": "Sector 12, Kharghar",
        "dept": "PWD Panvel",
        "stage": 1,  # 0=Reported 1=Verified 2=Assigned 3=Resolved
        "reported_on": "18 Aug 2026",
    },
    {
        "id": "NS-4468",
        "category": "Streetlight",
        "icon": "💡",
        "location": "Plot 44, Kalamboli",
        "dept": "Electrical Dept.",
        "stage": 2,
        "reported_on": "17 Aug 2026",
    },
    {
        "id": "NS-4459",
        "category": "Garbage",
        "icon": "🗑️",
        "location": "Sector 19, Nerul",
        "dept": "NMMC Sanitation",
        "stage": 3,
        "reported_on": "14 Aug 2026",
    },
    {
        "id": "NS-4432",
        "category": "Water leak",
        "icon": "💧",
        "location": "CBD Belapur",
        "dept": "Water Works",
        "stage": 3,
        "reported_on": "10 Aug 2026",
    },
]

STAGES = ["Reported", "Verified", "Assigned", "Resolved"]

# ---------------------------------------------------------------------------
# Styling — civic blue + marigold accent theme
# ---------------------------------------------------------------------------
NAVY = "#0F2A4A"
NAVY2 = "#123863"
MARIGOLD = "#FF9F1C"
MINT = "#1FAA76"
CORAL = "#E1543F"
AMBER = "#F5A524"
PAPER = "#F6F4EF"
MUTED = "#6B7684"
INK = "#0B1F33"
LINE = "#E7E3D9"

st.markdown(
    f"""
    <style>
        .stApp {{
            background: {PAPER};
        }}
        #MainMenu, header, footer {{visibility: hidden;}}

        .ns-hero {{
            background: linear-gradient(135deg, {NAVY} 0%, {NAVY2} 100%);
            padding: 34px 28px 40px;
            border-radius: 20px;
            margin-bottom: 24px;
        }}
        .ns-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 26px;
        }}
        .ns-brand-badge {{
            width: 36px; height: 36px;
            border-radius: 10px;
            background: {MARIGOLD};
            display: flex; align-items: center; justify-content: center;
            font-size: 18px;
        }}
        .ns-brand-name {{
            color: #fff; font-weight: 800; font-size: 18px;
        }}
        .ns-tagline {{
            color: #fff; font-size: 24px; font-weight: 800; line-height: 1.3; margin: 0;
        }}
        .ns-subtagline {{
            color: rgba(255,255,255,0.72); font-size: 13.5px; margin-top: 8px; max-width: 320px;
        }}

        .ns-card {{
            background: #fff;
            border: 1px solid {LINE};
            border-radius: 16px;
            padding: 16px 18px;
            margin-bottom: 12px;
        }}
        .ns-stat {{
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.14);
            border-radius: 14px;
            padding: 12px 6px;
            text-align: center;
        }}
        .ns-stat-num {{ color: #fff; font-size: 22px; font-weight: 800; margin: 0; }}
        .ns-stat-label {{ color: rgba(255,255,255,0.7); font-size: 11px; margin: 2px 0 0; }}

        .ns-badge {{
            display: inline-block;
            font-size: 10.5px;
            font-weight: 700;
            padding: 3px 9px;
            border-radius: 999px;
        }}

        .ns-stage-track {{ display: flex; align-items: center; margin: 12px 0 4px; }}
        .ns-dot {{
            width: 10px; height: 10px; border-radius: 50%;
        }}
        .ns-seg {{ flex: 1; height: 2px; margin: 0 2px; }}

        .ns-login-box {{
            background: #fff;
            border-radius: 20px;
            padding: 30px 28px;
            border: 1px solid {LINE};
            max-width: 380px;
            margin: 0 auto;
        }}

        div.stButton > button {{
            background: {MARIGOLD};
            color: {NAVY};
            font-weight: 700;
            border: none;
            border-radius: 12px;
            padding: 10px 0;
            width: 100%;
        }}
        div.stButton > button:hover {{
            background: #E88F0E;
            color: {NAVY};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------------------------------------------------------------------
# Login page
# ---------------------------------------------------------------------------
def render_login():
    st.markdown(
        f"""
        <div class="ns-hero">
            <div class="ns-brand">
                <div class="ns-brand-badge">🛡️</div>
                <div class="ns-brand-name">Nagar Sanchalak</div>
            </div>
            <p class="ns-tagline">Aapka Shehar,<br/>Aapki Zimmedari.</p>
            <p class="ns-subtagline">
                Photo kheecho, issue report karo — sahi department tak, seedha aur automatic.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ns-login-box">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:{INK}; margin-bottom:2px;'>Admin login</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{MUTED}; font-size:13px; margin-top:0;'>Dashboard dekhne ke liye login karein</p>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="admin")
    password = st.text_input("Password", placeholder="admin", type="password")

    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login safal — dashboard load ho raha hai...")
            time.sleep(0.4)
            st.rerun()
        else:
            st.error("Galat username ya password. Hint: admin / admin")

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Dashboard page
# ---------------------------------------------------------------------------
def stage_html(stage: int) -> str:
    dots = ""
    for i, label in enumerate(STAGES):
        color = MINT if i <= stage else LINE
        dots += f'<div class="ns-dot" style="background:{color};"></div>'
        if i < len(STAGES) - 1:
            seg_color = MINT if i < stage else LINE
            dots += f'<div class="ns-seg" style="background:{seg_color};"></div>'
    current_label = STAGES[stage]
    return f"""
        <div class="ns-stage-track">{dots}</div>
        <p style="font-size:11.5px; color:{INK}; font-weight:700; margin:0;">
            Current stage: <span style="color:{MINT};">{current_label}</span>
        </p>
    """


CATEGORY_COLOR = {
    "Pothole": CORAL,
    "Streetlight": "#1E6FD9",
    "Garbage": AMBER,
    "Water leak": MINT,
}


def render_dashboard():
    reported = sum(1 for i in ISSUES if i["stage"] == 0)
    in_progress = sum(1 for i in ISSUES if 0 < i["stage"] < 3)
    resolved = sum(1 for i in ISSUES if i["stage"] == 3)

    # Header
    col_l, col_r = st.columns([3, 1])
    with col_l:
        st.markdown(f"<p style='color:{MUTED}; font-size:12px; margin-bottom:0;'>Namaste,</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{INK}; font-size:20px; font-weight:800; margin-top:0;'>Admin</p>", unsafe_allow_html=True)
    with col_r:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown(
        f"""
        <div class="ns-hero" style="padding:20px 20px 22px; margin-bottom:18px;">
            <div style="display:flex; gap:10px;">
                <div class="ns-stat" style="flex:1;">
                    <p class="ns-stat-num">{reported}</p>
                    <p class="ns-stat-label">Reported</p>
                </div>
                <div class="ns-stat" style="flex:1;">
                    <p class="ns-stat-num">{in_progress}</p>
                    <p class="ns-stat-label">In progress</p>
                </div>
                <div class="ns-stat" style="flex:1;">
                    <p class="ns-stat-num">{resolved}</p>
                    <p class="ns-stat-label">Resolved</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Report new issue (mock uploader)
    st.markdown(f"<h4 style='color:{INK}; margin-bottom:6px;'>📷 Naya issue report karein</h4>", unsafe_allow_html=True)
    with st.expander("Photo upload karein aur details bharein", expanded=False):
        photo = st.file_uploader("Issue ki photo", type=["jpg", "jpeg", "png"])
        category = st.selectbox("Category", list(CATEGORY_COLOR.keys()))
        location = st.text_input("Location", placeholder="e.g. Sector 10, Kharghar")
        if st.button("Submit report"):
            if photo and location:
                st.success(f"Issue submit ho gaya! ID: NS-{4472 + len(ISSUES)} — {category} ko {location} ke liye route kiya ja raha hai.")
            else:
                st.warning("Photo aur location dono bharna zaroori hai.")

    st.markdown("---")

    # Recent issues
    st.markdown(f"<h4 style='color:{INK};'>📋 Recent reports</h4>", unsafe_allow_html=True)

    for issue in ISSUES:
        color = CATEGORY_COLOR[issue["category"]]
        st.markdown(
            f"""
            <div class="ns-card">
                <div style="display:flex; justify-content:space-between; align-items:baseline;">
                    <span style="font-weight:700; font-size:14.5px; color:{INK};">
                        {issue['icon']} {issue['category']}
                    </span>
                    <span style="font-size:11px; color:{MUTED}; font-family:monospace;">{issue['id']}</span>
                </div>
                <p style="margin:4px 0 0; font-size:12.5px; color:{MUTED};">📍 {issue['location']}</p>
                <p style="margin:1px 0 0; font-size:11.5px; color:{MUTED};">
                    Routed to <b style="color:{INK};">{issue['dept']}</b> · reported {issue['reported_on']}
                </p>
                {stage_html(issue['stage'])}
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------
if st.session_state.logged_in:
    render_dashboard()
else:
    render_login()