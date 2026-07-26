import streamlit as st
from PIL import Image
import os

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

st.set_page_config(page_title="Explainability", page_icon="")

st.title("🔍 Explainable AI")

st.write("""
This page shows how the machine learning model makes its decisions using:

- SHAP (Global Feature Importance)
- LIME (Local Prediction Explanation)
""")

st.markdown("---")

# SHAP Summary Plot
st.subheader("SHAP Summary Plot")

summary_path = "reports/explainability/shap_summary.png"

if os.path.exists(summary_path):
    image = Image.open(summary_path)
    st.image(image, use_container_width=True)
else:
    st.warning("SHAP Summary Plot not found.")

st.markdown("---")

# SHAP Bar Plot
st.subheader("SHAP Feature Importance")

bar_path = "reports/explainability/shap_bar.png"

if os.path.exists(bar_path):
    image = Image.open(bar_path)
    st.image(image, use_container_width=True)
else:
    st.warning("SHAP Bar Plot not found.")

st.markdown("---")

# LIME
st.subheader("LIME Explanation")

lime_path = "reports/explainability/lime_explanation.html"

if os.path.exists(lime_path):
    st.success("LIME explanation file generated successfully.")
    with open(lime_path, "r", encoding="utf-8") as f:
        st.download_button(
            label="Download LIME Explanation",
            data=f.read(),
            file_name="lime_explanation.html",
            mime="text/html"
        )
else:
    st.warning("LIME explanation not found.")