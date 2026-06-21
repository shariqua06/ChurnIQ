import streamlit as st
from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

load_css()
check_login()

df = load_data()

page_header("🔍 Customer Search", "Search customer records instantly")

customer_id = st.text_input("Enter Customer ID")

if customer_id:
    result = df[df["customerID"] == customer_id]

    if result.empty:
        st.warning("No customer found")
    else:
        st.dataframe(result)