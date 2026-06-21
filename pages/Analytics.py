import streamlit as st
import plotly.express as px

from src.utils import load_css
from src.security import check_login
from src.data_loader import load_data

load_css()
check_login()

st.title("📈 Analytics")

df = load_data()

st.markdown("""
<div style="
border:3px solid #ED9E59;
padding:15px;
border-radius:20px;
background:#44174E;
margin-bottom:20px;
">
<h3 style="color:white;">Customer Churn Distribution</h3>
</div>
""", unsafe_allow_html=True)

fig1 = px.pie(
    df,
    names="Churn",
    hole=0.6
)

fig1.update_traces(
    marker=dict(
        line=dict(
            color="black",
            width=2
        )
    ),
    textfont_size=18
)

fig1.update_layout(
    paper_bgcolor="white",
    height=550,
    font=dict(size=18)
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

fig2 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
    title="Contract Type vs Churn"
)

fig2.update_traces(
    marker_line_color="black",
    marker_line_width=1.5
)

fig2.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=550,
    font=dict(size=18)
)

st.plotly_chart(fig2, use_container_width=True)