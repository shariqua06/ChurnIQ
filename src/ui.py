import streamlit as st

def page_header(title, subtitle=None):

    st.markdown(f"""
    <div style="
        background:#44174E;
        padding:18px;
        border-radius:15px;
        border:2px solid #ED9E59;
        margin-bottom:20px;
    ">
        <h2 style="color:white; margin:0;">{title}</h2>
        <p style="color:#E9C8B9; margin:0;">{subtitle if subtitle else ""}</p>
    </div>
    """, unsafe_allow_html=True)


def card(title, value):

    st.markdown(f"""
    <div style="
        background:#1B1931;
        padding:15px;
        border-radius:12px;
        border:1px solid #ED9E59;
        text-align:center;
    ">
        <h4 style="color:#E9C8B9;">{title}</h4>
        <h2 style="color:white;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)