import pandas as pd
import streamlit as st
import plotly.express as px

from pathlib import Path



st.set_page_config(
    page_title="AI Behavioral Anomaly Detection",
    page_icon="",
    layout="wide"
)

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

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🛡️ AI Behavioral Anomaly Detection")

st.sidebar.markdown("---")

st.sidebar.success("Dashboard Navigation")

st.sidebar.info("""
📌 Modules

• Home

• Risk Analysis

• Explainability

• Live Prediction
""")

st.sidebar.markdown("---")

st.sidebar.write("### Project Information")

st.sidebar.write("**Dataset:** Synthetic Login Events")

st.sidebar.write("**Models:**")

st.sidebar.write("- Random Forest")

st.sidebar.write("- XGBoost")

st.sidebar.write("- LSTM")

st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")

st.markdown("""
<div class="hero-banner">

<h1 class="hero-title">
🛡 AI Behavioral Anomaly Detection
</h1>

<p style="font-size:18px;">
Real-time Cybersecurity Monitoring using Machine Learning,
Behavioral Profiling, Risk Scoring, SHAP and LIME
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"""
<div class="glass-card">

<h2>Project Overview</h2>

<p>
This project detects abnormal login behavior using Machine Learning,
Behavioral Profiling, Risk Scoring and Explainable AI.
</p>

</div>
""",
unsafe_allow_html=True
)

st.write("""
### Models Used
- Random Forest
- XGBoost
- LSTM

### Explainable AI
- SHAP
- LIME

### Features
- Behavioral Profiling
- Risk Scoring
- Anomaly Detection
- Explainable AI
""")

st.markdown("---")

st.markdown(
"""
<div class="section-title">
Dataset Statistics
</div>
""",
unsafe_allow_html=True
)

df = pd.read_csv("data/processed/features.csv")

total_events = len(df)

normal_events = (df["label"] == "Normal").sum()

anomalies = (df["label"] == "Anomaly").sum()

# If risk_score exists use its average
if "risk_score" in df.columns:
    avg_risk = df["risk_score"].mean()
else:
    avg_risk = 0

col1, col2, col3, col4 = st.columns(4)

cards = [
    ("Total Events", total_events),
    ("Normal", normal_events),
    ("Anomalies", anomalies),
    ("Avg Risk", round(avg_risk, 2))
]

for col, (label, value) in zip((col1, col2, col3, col4), cards):
    with col:
        st.markdown(f"""
        <div class="glass-card metric-card">
            <p class="metric-label">{label}</p>
            <p class="metric-value">{value}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown(
"""
<div class="section-title">
Data Visualizations
</div>
""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# -----------------------------
# Pie Chart
# -----------------------------
with col1:

    label_counts = df["label"].value_counts()

    fig = px.pie(
        values=label_counts.values,
        names=["Normal", "Anomaly"],
        title="Normal vs Anomaly"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Bar Chart
# -----------------------------
with col2:

    attack_counts = df["anomaly_type"].value_counts()

    fig = px.bar(
        x=attack_counts.index,
        y=attack_counts.values,
        title="Attack Distribution"
    )

    fig.update_layout(
        xaxis_title="Attack Type",
        yaxis_title="Count"
    )

    st.plotly_chart(fig, use_container_width=True)



st.markdown("---")

st.markdown(
"""
<div class="section-title">
Model Performance
</div>
""",
unsafe_allow_html=True
)

performance = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "LSTM"],
    "Accuracy": [0.9895, 0.9905, 0.9000],
    "Precision": [0.9893, 0.9918, 0.9888],
    "Recall": [1.0000, 0.9985, 0.9072],
    "F1 Score": [0.9946, 0.9951, 0.9462],
    "ROC AUC": [0.9715, 0.9522, 0.8636]
})

st.dataframe(
    performance,
    use_container_width=True
)

fig = px.bar(
    performance,
    x="Model",
    y="Accuracy",
    color="Model",
    title="Model Accuracy Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard Loaded Successfully!")

st.markdown("---")

st.markdown("""
<div class="footer">

AI Behavioral Anomaly Detection System

Version 1.0

Built with Python • Streamlit • XGBoost • TensorFlow • SHAP • LIME

</div>
""", unsafe_allow_html=True)