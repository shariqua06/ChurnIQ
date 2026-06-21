import streamlit as st
from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data

load_css()
check_login()

st.title("📊 ChurnIQ Dashboard")

df = load_data()

total_customers = len(df)
churned = len(df[df["Churn"] == "Yes"])
churn_rate = round((churned / total_customers) * 100, 2)
revenue = round(df["MonthlyCharges"].sum(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Customers", total_customers)

with col2:
    st.metric("⚠️ Churned", churned)

with col3:
    st.metric("📉 Churn Rate", f"{churn_rate}%")

with col4:
    st.metric("💰 Revenue", f"${revenue:,.0f}")

st.divider()

st.dataframe(df.head(), use_container_width=True)