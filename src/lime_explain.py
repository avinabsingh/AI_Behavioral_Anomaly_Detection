import os
import joblib
import pandas as pd

from lime.lime_tabular import LimeTabularExplainer

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("models/random_forest_model.pkl")

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("data/processed/features.csv")

X = df.drop(columns=["label", "anomaly_type"])
y = df["label"]

# -----------------------------
# Create LIME Explainer
# -----------------------------

explainer = LimeTabularExplainer(
    training_data=X.values,
    feature_names=X.columns.tolist(),
    class_names=["Anomaly", "Normal"],
    mode="classification"
)

# -----------------------------
# Explain One Sample
# -----------------------------

sample = X.iloc[0]

explanation = explainer.explain_instance(
    sample.values,
    model.predict_proba,
    num_features=10
)

# -----------------------------
# Save Explanation
# -----------------------------

os.makedirs(
    "reports/explainability",
    exist_ok=True
)

explanation.save_to_file(
    "reports/explainability/lime_explanation.html"
)

print("LIME Explanation Saved!")