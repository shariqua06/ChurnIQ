import streamlit as st
from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

load_css()
check_login()

df = load_data()

page_header("💰 Revenue Forecast", "Revenue insights overview")

total_revenue = df["MonthlyCharges"].sum()

st.metric("Total Revenue", f"${total_revenue:,.2f}")