# AI Behavioral Anomaly Detection System

> A enterprise-grade Machine Learning and Explainable AI (XAI) framework designed to identify, evaluate, and explain anomalous user login behaviors and cyber threat vectors in real time.

---

## Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Complete Project Workflow](#-complete-project-workflow)
- [Technology Stack](#-technology-stack)
- [Dataset Specifications](#-dataset-specifications)
- [Risk Scoring Mechanism](#-risk-scoring-mechanism)
- [Machine Learning Models](#-machine-learning-models)
- [Model Performance Comparison](#-model-performance-comparison)
- [Explainable AI (XAI) Integration](#-explainable-ai-xai-integration)
- [Dashboard & Visualization](#-dashboard--visualization)
- [Repository Structure](#-repository-structure)
- [Installation Guide](#-installation-guide)
- [Execution Pipeline](#-execution-pipeline)
- [Screenshots & Visuals](#-screenshots--visuals)
- [Project Highlights](#-project-highlights)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)
- [Authors & Maintainers](#-authors--maintainers)
- [Acknowledgements](#-acknowledgements)

---

## Overview

The **AI Behavioral Anomaly Detection System** is an end-to-end cybersecurity solution engineered to detect compromised credentials, insider threats, and automated attacks by analyzing authentication logs and user behavioral baselines. 

By combining traditional statistical risk scoring, ensemble machine learning, deep sequence modeling (LSTM), and state-of-the-art Explainable AI (SHAP & LIME), this platform moves beyond black-box detections—providing Security Operations Center (SOC) analysts with clear, interpretable rationale behind every flagged threat.

---

## Problem Statement

Modern cybersecurity landscapes suffer from three critical challenges:

1. **Volume and Velocity of Authentication Logs**: Security teams are overwhelmed by thousands of daily authentication events, leading to severe alert fatigue.
2. **Evolving Attack Vectors**: Sophisticated threats such as Credential Stuffing, Impossible Travel, and Lateral Movement frequently bypass static rule-based Intrusion Detection Systems (IDS).
3. **Black-Box AI Trust Deficit**: Advanced ML models flag anomalies with high accuracy, but fail to explain *why* an event was deemed suspicious, hindering rapid incident response.

This project resolves these bottlenecks by combining robust anomaly detection models with instant, human-understandable model explanations.

---

## Project Objectives

* **Behavioral Profiling**: Establish baseline normal behavior for every unique user based on historical authentication patterns, geographic markers, and device signatures.
* **Multi-Model Anomaly Detection**: Evaluate and compare statistical, tree-based ensemble, and deep temporal neural network architectures to achieve optimal detection accuracy.
* **Explainability First**: Integrate SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) to offer audit-ready threat intelligence.
* **Interactive SOC Operations**: Provide an interactive, multi-page Streamlit dashboard for real-time monitoring, threat hunting, and live inference.

---

## Key Features

* **Synthetic Event Generation**: Realistic log generation powered by `Faker` simulating standard traffic alongside advanced attack vectors.
* **Dynamic Behavioral Profiling**: Automated calculation of user-specific baselines across IP ranges, locations, authentication protocols, and device fingerprints.
* **Composite Risk Scoring**: Rule-guided heuristic scoring model to catch immediate structural anomalies before model inference.
* **Multi-Algorithm Model Suite**: Includes tuned implementations of **Random Forest**, **XGBoost**, and **LSTM (Long Short-Term Memory)** networks.
* **Dual-Layer Explainability**:
  * **Global Interpretability** via SHAP summary and feature importance plots.
  * **Local Interpretability** via LIME for granular event-level breakdown.
* **Interactive Streamlit Dashboard**: Full GUI covering live single-event prediction, historical risk analytics, downloadable PDF/JSON reports, and model explainability visualizers.

---

## System Architecture

The following diagram details the end-to-end data pipeline, machine learning engine, and visualization layers:

```mermaid
flowchart TD
    %% Node Definitions
    A[Synthetic Data Generator] --> B[Raw Data Validation Layer]
    B --> C[Feature Engineering & Extraction]
    C --> D[User Behavioral Profiling Engine]
    
    D --> E[Composite Risk Scoring Engine]
    
    E --> F1[Random Forest Classifier]
    E --> F2[XGBoost Classifier]
    E --> F3[LSTM Sequential Neural Network]
    
    F1 & F2 & F3 --> G[Evaluation & Model Selection]
    
    G --> H1[SHAP Global Explainability]
    G --> H2[LIME Local Explainability]
    
    H1 & H2 --> I[Streamlit Dashboard Interface]
    
    subgraph UI [SOC Analyst Operations]
        I --> J1[Home & Analytics Overview]
        I --> J2[Risk Analysis Dashboard]
        I --> J3[Explainability & SHAP/LIME Insights]
        I --> J4[Live Anomaly Predictor]
    end


# 🛡️ AI Behavioral Anomaly Detection for Cybersecurity

An end-to-end Machine Learning powered cybersecurity system that detects anomalous user login behavior using Behavioral Profiling, Risk Scoring, Explainable AI (SHAP & LIME), and an interactive Streamlit Dashboard.

---

# 📌 Project Workflow

```
Raw Data Generation
        │
        ▼
Data Validation & Quality Checks
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Feature Engineering
        │
        ▼
Behavioral Profile Generation
        │
        ▼
Risk Score Calculation
        │
        ▼
Model Training
(Random Forest • XGBoost • LSTM)
        │
        ▼
Model Evaluation
        │
        ▼
Explainable AI (SHAP & LIME)
        │
        ▼
Interactive Streamlit Dashboard
        │
        ▼
Real-Time Anomaly Prediction
```

---

# 💻 Technology Stack

## Programming Language
- Python 3.11+

## Machine Learning
- Scikit-learn
- XGBoost
- TensorFlow / Keras

## Explainable AI
- SHAP
- LIME

## Data Processing
- Pandas
- NumPy

## Visualization
- Matplotlib
- Plotly
- Streamlit

## Model Persistence
- Joblib

## Development Environment
- Jupyter Notebook
- VS Code

---

# 📂 Dataset Specifications

Since publicly available datasets do not fully capture organization-specific behavioral patterns, a realistic synthetic dataset was generated.

| Property | Value |
|-----------|-------|
| Total Login Events | 10,000 |
| Normal Events | 9,700 |
| Anomalies | 300 |
| Anomaly Ratio | 3% |
| Users | Multiple simulated users |
| Dataset Type | Synthetic |
| Data Format | CSV |

---

# 🚨 Simulated Threat Vectors

The synthetic dataset contains multiple real-world cybersecurity attack scenarios.

| Threat | Description |
|----------|-------------|
| Brute Force Attack | Multiple failed login attempts |
| Credential Stuffing | Stolen credentials used for authentication |
| Impossible Travel | Login from geographically impossible locations |
| Device Spoofing | Login from an unknown device fingerprint |
| Lateral Movement | Access to unusual internal resources |
| Data Exfiltration | Abnormally long sessions accessing sensitive resources |

---

# 📊 Dataset Feature Schema

| Feature | Description |
|----------|-------------|
| entity_id | Unique user identifier |
| entity_type | Employee, Admin, Contractor, Service Account |
| geo_location | User login country/location |
| auth_method | Password, MFA, Biometric, OAuth |
| resource_accessed | System resource being accessed |
| session_duration | Login session duration (seconds) |
| login_status | Success / Failed |
| protocol | HTTPS, SSH, FTP, HTTP |
| device_fingerprint | Unique registered device |
| hour | Login hour |
| day | Day of month |
| month | Month |
| weekday | Day of week |
| label | Normal / Anomaly |
| anomaly_type | Type of simulated cyber attack |

---

# ⚠️ Risk Scoring Mechanism

Behavioral risk is calculated by comparing each login event against the user's historical profile.

Each suspicious activity increases the cumulative risk score.

```
Final Risk Score =
Country Risk
+ Authentication Risk
+ Protocol Risk
+ Resource Risk
+ Device Risk
+ Session Duration Risk
```

Higher scores indicate a greater probability of malicious behavior.

---

# 🎯 Evaluated Risk Factors & Weight Distribution

| Risk Factor | Weight |
|--------------|--------|
| Unknown Geo Location | +30 |
| Unknown Device | +25 |
| Long Session Duration | +20 |
| Authentication Method Change | +15 |
| Sensitive Resource Access | +15 |
| Suspicious Network Protocol | +10 |

Maximum Possible Risk Score: **115**

---

# 🤖 Machine Learning Models

Three different models were trained and evaluated.

## 1. Random Forest

- Ensemble Learning
- Handles mixed feature types
- Robust against overfitting
- High interpretability

---

## 2. XGBoost

- Gradient Boosted Decision Trees
- Excellent predictive performance
- Fast inference
- Strong handling of nonlinear relationships

---

## 3. LSTM Neural Network

- Deep Learning model
- Learns sequential behavioral patterns
- Suitable for temporal login analysis

---

# 📈 Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|--------|-----------|-----------|---------|----------|----------|
| Random Forest | **98.95%** | 98.93% | 100.00% | 99.46% | **97.15%** |
| XGBoost | **99.05%** | **99.18%** | 99.85% | **99.51%** | 95.22% |
| LSTM | 90.00% | 98.88% | 90.72% | 94.62% | 86.36% |

### Best Performing Model

**Random Forest** was selected for deployment due to its excellent balance of:
- High accuracy
- Fast prediction time
- Robustness
- Better interpretability

---

# 🧠 Explainable AI (XAI) Integration

To improve transparency and trust, Explainable AI techniques are integrated.

## SHAP (SHapley Additive Explanations)

Provides:
- Global feature importance
- Local prediction explanations
- Feature contribution analysis
- SHAP Summary Plot
- SHAP Bar Plot

---

## LIME (Local Interpretable Model-Agnostic Explanations)

Provides:
- Instance-level prediction explanations
- Human-readable decision reasoning
- Feature contribution visualization

---

# 📊 Dashboard & Visualization

The project includes a modern Streamlit dashboard.

## Home Dashboard

- Dataset Overview
- KPI Cards
- Attack Distribution
- Model Performance Comparison
- Interactive Charts

---

## Risk Analysis

- Highest Risk Events
- Average Risk Score
- Lowest Risk Score
- Risk Distribution
- Top High-Risk Login Attempts

---

## Explainability

- SHAP Summary Plot
- SHAP Feature Importance
- LIME Explanation Report

---

## Live Prediction

Real-time prediction interface with:

- User Login Simulation
- Behavioral Risk Prediction
- Confidence Score
- Risk Level
- AI Explanation
- Security Recommendation
- Login Summary
- Feature Risk Analysis
- Interactive Visualization

---

# 🚀 Key Features

- Synthetic Cybersecurity Dataset Generation
- Behavioral User Profiling
- Dynamic Risk Scoring
- Machine Learning-Based Detection
- Explainable AI Integration
- Interactive Dashboard
- Real-Time Login Prediction
- Security Recommendations
- Feature Importance Visualization
- Professional UI with Streamlit

---

# 📁 Project Structure

```
AI_Behavioral_Anomaly_Detection/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│
├── dashboard/
│   ├── app.py
│   ├── assets/
│   └── pages/
│
├── models/
│
├── notebooks/
│
├── reports/
│   ├── explainability/
│   ├── evaluation/
│   └── data_quality/
│
├── src/
│
└── README.md
```

---

# 🎯 Future Enhancements

- Real-time SIEM Integration
- Live Network Traffic Monitoring
- Kafka-based Streaming Pipeline
- Graph Neural Networks (GNN)
- Online Learning Models
- User Behavior Analytics (UBA)
- Cloud Deployment (AWS/Azure/GCP)
- Multi-Factor Risk Engine
- Threat Intelligence Integration
- Automated Incident Response
