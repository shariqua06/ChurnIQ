import os
import streamlit as st

def load_css():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_path = os.path.join(BASE_DIR, "assets", "styles.css")

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)