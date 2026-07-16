from typing import Dict, List

import pandas as pd


def recommend_ml_problem_type(problem_description: str) -> Dict:
    """
    Recommend the ML problem type based on the user's description.
    """

    text = problem_description.lower()

    if "churn" in text or "yes/no" in text or "fraud" in text:
        return {
            "problem_type": "classification",
            "reason": "Binary outcome prediction."
        }

    elif "price" in text or "sales" in text or "revenue" in text:
        return {
            "problem_type": "regression",
            "reason": "Predicting a continuous value."
        }

    elif "forecast" in text or "future" in text:
        return {
            "problem_type": "forecasting",
            "reason": "Time-series prediction."
        }

    elif "group" in text or "segment" in text:
        return {
            "problem_type": "clustering",
            "reason": "Grouping similar records."
        }

    else:
        return {
            "problem_type": "anomaly_detection",
            "reason": "Detect unusual behaviour."
        }


def suggest_feature_engineering(columns: List[str]) -> Dict:
    """
    Suggest feature engineering ideas based on column names.
    """

    features = []

    if "transaction_date" in columns:
        features.extend([
            "Day of Week",
            "Month",
            "Quarter"
        ])

    if "customer_id" in columns:
        features.extend([
            "Purchase Frequency",
            "Days Since Last Purchase"
        ])

    if "revenue" in columns:
        features.extend([
            "Rolling Average Revenue",
            "Revenue Growth Rate"
        ])

    if "event_time" in columns:
        features.extend([
            "Events per Hour",
            "Peak Activity Time"
        ])

    if not features:
        features.append("Standard Scaling")

    return {
        "recommended_features": features
    }


def detect_ml_data_risks(df: pd.DataFrame) -> Dict:
    """
    Detect common ML data risks.
    """

    risks = []

    if df.isnull().sum().sum() > 0:
        risks.append("Missing values detected")

    if df.duplicated().sum() > 0:
        risks.append("Duplicate rows detected")

    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:

        if df[col].nunique() > len(df) * 0.8:
            risks.append(f"High-cardinality column: {col}")

    return {
        "identified_risks": risks
    }


def recommend_evaluation_metrics(problem_type: str) -> Dict:
    """
    Recommend evaluation metrics.
    """

    metrics = {

        "classification": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1-score",
            "ROC-AUC"
        ],

        "regression": [
            "RMSE",
            "MAE",
            "R²"
        ],

        "forecasting": [
            "MAPE",
            "RMSE",
            "SMAPE"
        ],

        "clustering": [
            "Silhouette Score",
            "Davies-Bouldin Index"
        ],

        "anomaly_detection": [
            "Precision",
            "Recall",
            "ROC-AUC"
        ]

    }

    return {
        "problem_type": problem_type,
        "metrics": metrics.get(problem_type, [])
    }


def create_ml_pipeline_plan() -> Dict:
    """
    Create a standard ML pipeline.
    """

    return {

        "pipeline": [

            "Data Ingestion",

            "Data Validation",

            "Data Cleaning",

            "Feature Engineering",

            "Train-Test Split",

            "Model Training",

            "Model Evaluation",

            "Hyperparameter Tuning",

            "Model Registry",

            "Deployment",

            "Monitoring",

            "Retraining"

        ]
    }