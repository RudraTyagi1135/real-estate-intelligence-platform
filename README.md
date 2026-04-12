# Gurgaon Real Estate Intelligence System

End-to-end notebook-driven machine learning project for Gurgaon residential real estate. The repository covers data collection, cleaning, feature engineering, outlier treatment, missing-value handling, feature selection, model training, recommender preparation, insight generation, and a Streamlit app for prediction and analytics.

This is not a toy notebook dump. The repo contains the full working pipeline artifacts that feed the app:

- raw scraped property data
- cleaned and merged datasets
- engineered and model-ready datasets
- serialized prediction pipeline assets
- recommender similarity assets
- Streamlit pages for price prediction, analytics, and apartment recommendation

## What This Project Does

The system is built around three practical outputs:

1. Price prediction for Gurgaon properties through a trained scikit-learn pipeline.
2. Interactive market analytics through a Streamlit dashboard backed by prepared visualization data.
3. Apartment recommendation and radius-based location search using similarity matrices and a location-distance table.

## Repository Workflow

The folders are numbered to show the execution flow.

| Stage | Folder | Purpose | Main Output |
| --- | --- | --- | --- |
| 0 | `000_web_scraping` | Scrape apartment, flats, independent house, and residential land data | raw CSV files |
| 1 | `001_raw_data` | Raw source datasets | `apartment.csv`, `flats.csv`, `independent_house.csv`, `residential_land.csv` |
| 2 | `002_data_preprocessing` | Clean flats and houses, then merge them | cleaned intermediate CSVs |
| 3 | `003_cleaned_data` | Consolidated cleaned data | merged and cleaned Gurgaon property datasets |
| 4 | `004_feature_engineering` | Create derived features and structured model inputs | featured dataset |
| 5 | `005_featured_data` | Engineered data store | `01_gurgaon_properties_featured.csv` |
| 6 | `006_EDA` | Univariate, profiling, and multivariate analysis | EDA notebooks |
| 7 | `007_outlier_detection_and_removal` | Detect and treat outliers | outlier-treated dataset |
| 8 | `008_outlier_treated_data` | Post-outlier dataset | `gurgaon_properties_outlier_treated.csv` |
| 9 | `009_missing_value_imputation` | Impute missing values and reduce schema noise | imputed dataset |
| 10 | `010_missing_value_imputed_data` | Post-imputation dataset | `gurgaon_properties_missing_value_imputed.csv` |
| 11 | `011_feature_selection` | Select final model features | reduced feature dataset |
| 12 | `012_post_feature_selection_data` | Final training datasets | v1 and v2 post-feature-selection CSVs |
| 13 | `013_baseline_model` | Train baseline models for comparison | baseline experiments |
| 14 | `014_model_selection` | Evaluate and select the final modeling pipeline | selected model candidate |
| 15 | `015_selected_model_and_preprocessor` | Final serialized prediction assets | `df.pkl`, `pipeline.pkl` |
| 16 | `016_real_estate_website` | Streamlit application | prediction, analytics, recommendation UI |
| 17 | `017_extras_for_analytics_module` | Support files for app analytics | `latlong.csv`, `data_viz` preparation notebook |
| 18 | `018_recommender_system` | Similarity and recommendation preparation | recommender assets |
| 19 | `019_insight_module` | Insight generation notebook | summary analysis notebook |

## Actual Data and Artifact Inventory

### Raw data

| File | Shape |
| --- | --- |
| `001_raw_data/apartment.csv` | 247 rows x 7 cols |
| `001_raw_data/flats.csv` | 3028 rows x 20 cols |
| `001_raw_data/independent_house.csv` | 1095 rows x 21 cols |
| `001_raw_data/residential_land.csv` | present |

### Processed datasets

| File | Shape |
| --- | --- |
| `003_cleaned_data/03_gurgaon_properties.csv` | 3962 rows x 20 cols |
| `003_cleaned_data/04_gurgaon_properties_cleaned.csv` | present |
| `005_featured_data/01_gurgaon_properties_featured.csv` | 3803 rows x 23 cols |
| `008_outlier_treated_data/gurgaon_properties_outlier_treated.csv` | 3555 rows x 24 cols |
| `010_missing_value_imputed_data/gurgaon_properties_missing_value_imputed.csv` | 3554 rows x 18 cols |
| `012_post_feature_selection_data/gurgaon_properties_post_feature_selection.csv` | 3554 rows x 13 cols |
| `012_post_feature_selection_data/gurgaon_properties_post_feature_selection_v2.csv` | 3554 rows x 13 cols |

### Prediction artifacts

`015_selected_model_and_preprocessor` contains:

- `df.pkl`: 3554 rows x 12 cols
- `pipeline.pkl`: serialized `sklearn.pipeline.Pipeline`

Model input features exposed by `df.pkl`:

- `property_type`
- `sector`
- `bedRoom`
- `bathroom`
- `balcony`
- `agePossession`
- `built_up_area`
- `servant room`
- `store room`
- `furnishing_type`
- `luxury_category`
- `floor_category`

### Streamlit analytics and recommender assets

`016_real_estate_website/datasets` contains:

- `data_viz1.csv`: 3329 rows x 21 cols
- `feature_text.pkl`: serialized feature corpus string for word cloud generation
- `location_distance.pkl`: `pandas.DataFrame`, shape `(246, 1070)`
- `cosine_sim1.pkl`: `numpy.ndarray`, shape `(246, 246)`
- `cosine_sim2.pkl`: `numpy.ndarray`, shape `(246, 246)`
- `cosine_sim3.pkl`: `numpy.ndarray`, shape `(246, 246)`

`017_extras_for_analytics_module` contains:

- `01_data_visualization.ipynb`
- `02_latlong_scraper.py`
- `latlong.csv`

## Streamlit App

The application lives in `016_real_estate_website`.

### Live deployment

[Streamlit App](https://homepy-aggrqej8vtvemzm3japd32.streamlit.app/)

### Pages

- `home.py`: app entrypoint
- `pages/1_price_predictor.py`: predicts a price range using the serialized pipeline
- `pages/2_analysis_app.py`: sector map, word cloud, area-vs-price plots, BHK mix, and price distribution views
- `pages/3_recommended_apartments.py`: radius-based location search and apartment recommendations

### Run the app

```bash
streamlit run 016_real_estate_website/home.py
```

## Notebooks Included

The repo currently contains 20 notebooks:

- `000_web_scraping/apartments.ipynb`
- `000_web_scraping/flats.ipynb`
- `000_web_scraping/Independent_house.ipynb`
- `000_web_scraping/residential_land.ipynb`
- `002_data_preprocessing/01_data_preprocessing_flats.ipynb`
- `002_data_preprocessing/02_data_preprocessing_houses.ipynb`
- `002_data_preprocessing/03_merge_flats_and_house.ipynb`
- `002_data_preprocessing/04_data_preprocessing_after_merge.ipynb`
- `004_feature_engineering/01_feature_engineering.ipynb`
- `006_EDA/01_eda_univariate_analysis.ipynb`
- `006_EDA/02_eda_pandas_profiling.ipynb`
- `006_EDA/03_eda_multivariate_analysis.ipynb`
- `007_outlier_detection_and_removal/01_outlier_treatment.ipynb`
- `009_missing_value_imputation/01_missing_value_imputation.ipynb`
- `011_feature_selection/01_feature_selection.ipynb`
- `013_baseline_model/baseline_model.ipynb`
- `014_model_selection/01_model_selection.ipynb`
- `017_extras_for_analytics_module/01_data_visualization.ipynb`
- `018_recommender_system/01_recommender_system.ipynb`
- `019_insight_module/01_insights_module.ipynb`

## Tech Stack

- Python 3.11
- Pandas
- NumPy
- scikit-learn
- SciPy
- XGBoost
- category-encoders
- SHAP
- Matplotlib
- Seaborn
- Plotly
- ydata-profiling
- Streamlit
- Beautiful Soup 4
- WordCloud
- Jupyter / IPykernel

Dependencies are pinned in `requirements.txt`.

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd GURGAON_REAL_ESTATE_INTELLIGENCE_SYSTEM
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter or Streamlit

```bash
jupyter notebook
```

or

```bash
streamlit run 016_real_estate_website/home.py
```

## Recommended Execution Order

If you want to reproduce the project flow from scratch, use the folders in numeric order:

1. `000_web_scraping`
2. `002_data_preprocessing`
3. `004_feature_engineering`
4. `006_EDA`
5. `007_outlier_detection_and_removal`
6. `009_missing_value_imputation`
7. `011_feature_selection`
8. `013_baseline_model`
9. `014_model_selection`
10. `017_extras_for_analytics_module`
11. `018_recommender_system`
12. `019_insight_module`

The serialized prediction assets and app datasets already exist in the repo, so the app can be run without retraining if those files remain intact.

## What Is In Scope

- Gurgaon residential property data pipeline
- notebook-based data processing and modeling workflow
- model artifact persistence for app inference
- analytics dashboard inputs and plots
- apartment recommendation support assets
- reproducible local execution with pinned dependencies

## What Is Not In Scope

- packaged Python library structure
- REST API or backend service layer
- automated training pipeline orchestration
- test suite or CI pipeline
- cloud deployment configuration
- production data validation or monitoring framework
- database-backed serving infrastructure

## Current Constraints

This repository is functional, but it is still notebook-first. That has concrete implications:

- transformation logic is spread across notebooks instead of reusable modules
- there is no automated retraining command
- model and recommender generation depend on sequential notebook execution
- app startup assumes required artifacts already exist
- there is no formal experiment tracking or model registry

## If You Want To Productionize This

The next engineering steps would be:

1. Extract notebook logic into importable Python modules.
2. Add a single reproducible pipeline entrypoint for rebuilds.
3. Add tests for schema, transformations, and inference behavior.
4. Separate training artifacts from app-serving assets.
5. Add config management and environment-specific paths.
6. Add deployment and monitoring around the Streamlit app or a service API.

## Author

**Rudra**  
ML Systems / AI Infrastructure Engineer
