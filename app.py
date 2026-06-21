import streamlit as st
from src.database import create_database

st.set_page_config(
    page_title="ChurnIQ",
    page_icon="📊",
    layout="wide"
)

create_database()

st.title("ChurnIQ")
st.subheader("AI-Powered Customer Retention Intelligence Platform")

st.success("Database initialized successfully!")