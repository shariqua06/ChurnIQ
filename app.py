import streamlit as st
import os

from src.database import create_database
from src.auth import authenticate_user
from src.utils import load_css

# -------------------------
# BASE SETUP
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="ChurnIQ",
    page_icon="📊",
    layout="wide"
)

load_css()

# Create DB safely (only once per session)
if "db_created" not in st.session_state:
    create_database()
    st.session_state.db_created = True

# -------------------------
# SESSION STATE
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "email" not in st.session_state:
    st.session_state.email = None


# -------------------------
# LOGOUT FUNCTION
# -------------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.email = None
    st.rerun()


# -------------------------
# LOGIN PAGE
# -------------------------
if not st.session_state.logged_in:

    st.title("ChurnIQ")
    st.subheader("AI-Powered Customer Retention Intelligence Platform")

    st.markdown("---")

    st.info("""
Demo Credentials

Admin: admin@churniq.com / Admin@123  
Analyst: analyst@churniq.com / Analyst@123  
Viewer: viewer@churniq.com / Viewer@123
""")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        role = authenticate_user(email, password)

        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Invalid Email or Password")

# -------------------------
# MAIN APP
# -------------------------
else:

    st.title("ChurnIQ Dashboard")

    st.success(f"Logged in as {st.session_state.email} ({st.session_state.role})")

    # =========================
    # SIDEBAR LOGOUT (NEW)
    # =========================
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.email}")
        st.markdown(f"Role: {st.session_state.role}")
        st.markdown("---")

        if st.button("🚪 Logout"):
            logout()

    st.markdown("---")

    # HERO SECTION
    st.markdown("### Welcome to ChurnIQ")
    st.write("AI-powered customer analytics platform for churn prediction, insights, and business intelligence.")

    st.markdown("---")

    # QUICK INFO CARDS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("Analytics\nCustomer trends & patterns")

    with col2:
        st.info("Prediction\nReal-time churn prediction")

    with col3:
        st.info("Explainability\nUnderstand AI decisions")

    st.markdown("---")

    # SESSION CONTROL (KEEP OLD ONE ALSO AS YOU REQUESTED)
    st.markdown("### Session Control")

    colA, colB = st.columns([1, 5])

    with colA:
        if st.button("Logout"):
            logout()

    with colB:
        st.markdown("#### Secure logout from ChurnIQ session")