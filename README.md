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