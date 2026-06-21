import streamlit as st
from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data
from src.ui import page_header

load_css()
check_login()

df = load_data()

page_header("📄 Reports", "Complete dataset summary")

st.markdown("### Dataset Overview")
st.write("Total Customers:", len(df))
st.write("Churned Customers:", len(df[df["Churn"] == "Yes"]))

st.markdown("### Sample Data")
st.dataframe(df.head(20))