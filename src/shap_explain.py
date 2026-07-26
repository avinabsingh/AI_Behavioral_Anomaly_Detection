import os
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("models/random_forest_model.pkl")

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("data/processed/features.csv")

X = df.drop(columns=["label", "anomaly_type"])

# -----------------------------
# Create SHAP Explainer
# -----------------------------

explainer = shap.TreeExplainer(model)

# -----------------------------
# Calculate SHAP Values
# -----------------------------

shap_values = explainer.shap_values(X)

# -----------------------------
# Create Folder
# -----------------------------

os.makedirs("reports/explainability", exist_ok=True)

# -----------------------------
# Summary Plot
# -----------------------------

plt.figure(figsize=(10,6))

shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.tight_layout()

plt.savefig(
    "reports/explainability/shap_summary.png",
    dpi=300
)

plt.close()

print("SHAP Summary Plot Saved!")

# -----------------------------
# Bar Plot
# -----------------------------

plt.figure(figsize=(10,6))

shap.summary_plot(
    shap_values,
    X,
    plot_type="bar",
    show=False
)

plt.tight_layout()

plt.savefig(
    "reports/explainability/shap_bar.png",
    dpi=300
)

plt.close()

print("SHAP Bar Plot Saved!")