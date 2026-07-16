from pathlib import Path

import pandas as pd


def mcp_detect_data_quality_issues(file_path: str):
    """
    Detect common data quality issues in a CSV file.

    Checks:
    - Missing values
    - Duplicate rows
    - Constant columns
    - High-cardinality columns
    """

    df = pd.read_csv(Path(file_path))

    issues = {}

    # Missing values
    issues["missing_values"] = df.isna().sum().to_dict()

    # Duplicate rows
    issues["duplicate_rows"] = int(df.duplicated().sum())

    # Constant columns
    issues["constant_columns"] = []

    for col in df.columns:
        if df[col].nunique(dropna=False) == 1:
            issues["constant_columns"].append(col)

    # High-cardinality columns
    issues["high_cardinality_columns"] = []

    # Columns that are naturally unique should not be treated as data quality issues
    ignored_columns = {
        "id",
        "customer_id",
        "order_id",
        "product_id",
        "transaction_id",
        "user_id",
        "employee_id",
        "name",
        "customer_name",
        "first_name",
        "last_name",
        "email",
        "phone"
    }

    for col in df.select_dtypes(include="object").columns:

        if col.lower() in ignored_columns:
            continue

        uniqueness_ratio = df[col].nunique() / len(df)

        if uniqueness_ratio > 0.80:
            issues["high_cardinality_columns"].append(col)

    return issues