import pandas as pd

# Load dataset
df = pd.read_csv("data/synthetic/login_events.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Users:")
print(df["entity_id"].nunique())

print("\nLabel Distribution:")
print(df["label"].value_counts())

print("\nAttack Distribution:")
print(df["anomaly_type"].value_counts())

print("\nLogin Status:")
print(df["login_status"].value_counts())

print("\nProtocol Distribution:")
print(df["protocol"].value_counts())

print("\nCountry Distribution:")
print(df["geo_location"].value_counts())


import json
import os

report = {
    "Rows": int(df.shape[0]),
    "Columns": int(df.shape[1]),
    "Duplicate Rows": int(df.duplicated().sum()),
    "Unique Users": int(df["entity_id"].nunique()),
    "Missing Values": df.isnull().sum().to_dict(),
    "Label Distribution": df["label"].value_counts().to_dict(),
    "Attack Distribution": df["anomaly_type"].value_counts().to_dict()
}

os.makedirs("reports/data_quality", exist_ok=True)

with open("reports/data_quality/data_quality_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nData quality report saved successfully!")