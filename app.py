import streamlit as st
from src.database import create_database
from src.auth import authenticate_user
from src.utils import load_css

st.set_page_config(
    page_title="ChurnIQ",
    page_icon="📊",
    layout="wide"
)

load_css()

create_database()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "email" not in st.session_state:
    st.session_state.email = None


def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.email = None
    st.rerun()


if not st.session_state.logged_in:

    st.title("📊 ChurnIQ")
    st.subheader("AI-Powered Customer Retention Intelligence Platform")

    st.info("""
Demo Credentials

Admin
Email: admin@churniq.com
Password: Admin@123

Analyst
Email: analyst@churniq.com
Password: Analyst@123

Viewer
Email: viewer@churniq.com
Password: Viewer@123
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

else:

    st.success(
        f"Logged in as {st.session_state.email} ({st.session_state.role})"
    )

    st.title("ChurnIQ Dashboard")

    st.write("Welcome to ChurnIQ.")

    if st.button("Logout"):
        logout()