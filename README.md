# Real Estate Intelligence Platform

End-to-end machine learning and analytics platform for Gurgaon residential real estate focused on price prediction, market analytics, and apartment recommendation workflows.

The project combines:
- large-scale property data collection
- feature engineering pipelines
- predictive modeling
- recommendation systems
- interactive Streamlit analytics dashboards

This repository represents a complete applied ML workflow — from raw data acquisition to deployable analytics applications.

---

# Project Overview

The platform is built around three primary capabilities:

### Price Prediction
Predicts Gurgaon residential property prices using a trained scikit-learn pipeline with engineered real estate features.

### Market Analytics
Interactive Streamlit dashboards for:
- sector-level pricing analysis
- BHK distribution analysis
- price trends
- area vs price analysis
- geographic insights
- feature-driven visualization

### Apartment Recommendation
Recommendation engine using:
- similarity matrices
- location-distance calculations
- radius-based apartment discovery

---

# System Workflow

```text
Web Scraping
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
Outlier Treatment
      ↓
Missing Value Imputation
      ↓
Feature Selection
      ↓
Model Training & Evaluation
      ↓
Serialized Prediction Pipeline
      ↓
Streamlit Analytics Application
      ↓
Recommendation System
```

---

# Core Features

- End-to-end ML workflow
- Real estate price prediction
- Interactive analytics dashboards
- Recommendation engine
- Serialized sklearn inference pipeline
- Feature engineering pipeline
- Similarity-based apartment recommendation
- Streamlit deployment workflow
- Reproducible local execution

---

# Tech Stack

## Machine Learning
- scikit-learn
- XGBoost
- SHAP
- SciPy
- category-encoders

## Data Processing
- Pandas
- NumPy

## Visualization & Analytics
- Plotly
- Matplotlib
- Seaborn
- WordCloud
- ydata-profiling

## Application Layer
- Streamlit

## Data Collection
- BeautifulSoup4

---

# Repository Structure

```text
real-estate-intelligence-platform/

├── 000_web_scraping/
├── 002_data_preprocessing/
├── 004_feature_engineering/
├── 006_EDA/
├── 007_outlier_detection_and_removal/
├── 009_missing_value_imputation/
├── 011_feature_selection/
├── 013_baseline_model/
├── 014_model_selection/
├── 015_selected_model_and_preprocessor/
├── 016_real_estate_website/
├── 017_extras_for_analytics_module/
├── 018_recommender_system/
└── 019_insight_module/
```

---

# Streamlit Application

The application includes:

### Price Prediction Module
Predicts property prices using the trained inference pipeline.

### Analytics Dashboard
Interactive visualizations for:
- sector pricing
- BHK distribution
- luxury category analysis
- geographic trends
- market segmentation

### Recommendation Engine
Apartment recommendation workflow using:
- cosine similarity matrices
- location proximity calculations
- radius-based recommendation logic

---

# Running The Application

## Clone Repository

```bash
git clone <your-repository-url>
cd real-estate-intelligence-platform
```

---

## Create Virtual Environment

### Windows PowerShell

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Launch Streamlit App

```bash
streamlit run 016_real_estate_website/home.py
```

---

# Engineering Highlights

- Full ML workflow ownership from data acquisition to inference
- Serialized sklearn prediction pipeline
- Recommendation system integration
- Interactive analytics deployment
- Large-scale feature engineering workflow
- End-to-end reproducible ML project structure
- Applied real-world dataset handling
- Multi-stage data transformation pipeline

---

# Current Architecture Status

This repository is currently:
- notebook-driven
- modular by workflow stage
- optimized for reproducible experimentation and analytics

The system is functional and deployable locally, but not yet structured as a fully productionized ML service architecture.

---

# Current Limitations

Current constraints include:

- notebook-centric workflow organization
- no centralized pipeline orchestration
- no REST API serving layer
- no CI/CD pipeline
- no automated retraining workflow
- no experiment tracking integration
- no cloud deployment workflow

---

# Planned Engineering Improvements

Future engineering improvements include:

- modular Python package refactoring
- FastAPI inference service
- automated retraining pipeline
- CI/CD integration
- deployment workflows
- experiment tracking
- containerized deployment
- configuration management

---

# Author

Rudra Tyagi

Focus Areas:
- ML Engineering
- MLOps
- Cloud AI Systems
- Applied Machine Learning
- AI Infrastructure Engineering
