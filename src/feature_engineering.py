import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/synthetic/login_events.csv")

print(df.head())

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extract useful time features
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df["month"] = df["timestamp"].dt.month
df["weekday"] = df["timestamp"].dt.weekday

# Drop original timestamp
df.drop(columns=["timestamp"], inplace=True)

df.drop(
    columns=[
        "source_ip",
        "command_sequence"
    ],
    inplace=True
)

label_encoders = {}

categorical_columns = [
    "entity_id",
    "entity_type",
    "geo_location",
    "resource_accessed",
    "auth_method",
    "login_status",
    "device_fingerprint",
    "protocol",
    "label",
    "anomaly_type"
]

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder


import joblib

os.makedirs("models", exist_ok=True)

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

print("Label Encoders Saved")


os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/features.csv",
    index=False
)

print("Processed Dataset Saved")

print("\nFinal Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())