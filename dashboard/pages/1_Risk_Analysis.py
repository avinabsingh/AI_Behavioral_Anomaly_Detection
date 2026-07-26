import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"

    if not css_path.exists():
        css_path = Path(__file__).parent.parent / "assets" / "style.css"

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.set_page_config(page_title="Risk Analysis", page_icon="")

st.title("Risk Score Analysis")

# Load Data
df = pd.read_csv("data/processed/risk_scored_events.csv")

st.write("This page analyzes the calculated risk scores for user login events.")

# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Highest Risk", int(df["risk_score"].max()))

with col2:
    st.metric("Average Risk", round(df["risk_score"].mean(), 2))

with col3:
    st.metric("Lowest Risk", int(df["risk_score"].min()))

st.markdown("---")

# Histogram
fig = px.histogram(
    df,
    x="risk_score",
    nbins=20,
    title="Risk Score Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Highest-risk events
st.subheader("Top 10 Highest Risk Events")

top10 = df.sort_values(
    by="risk_score",
    ascending=False
).head(10)

st.dataframe(top10, use_container_width=True)