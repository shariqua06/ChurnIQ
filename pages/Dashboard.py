import streamlit as st
from src.utils import load_css

load_css()

st.title("📊 ChurnIQ Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", "7043")

with col2:
    st.metric("Churn Rate", "26.5%")

with col3:
    st.metric("Revenue", "$16.1M")

with col4:
    st.metric("High Risk", "1869")

st.divider()

st.info("Dashboard UI Phase 1")