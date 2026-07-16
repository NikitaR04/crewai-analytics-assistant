import re
from typing import Dict, List

import pandas as pd


def profile_dataframe(data) -> Dict:
    """
    Profile a DataFrame or CSV file.
    """

    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data.copy()

    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "data_types": {k: str(v) for k, v in df.dtypes.items()},
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "sample_records": df.head(5).to_dict(orient="records")
    }


def suggest_kpi_metrics(domain: str, columns: List[str]) -> Dict:
    """
    Suggest KPIs based on business domain.
    """

    domain = domain.lower()

    kpis = {
        "ecommerce": [
            "Total Revenue",
            "Average Order Value",
            "Monthly Sales",
            "Repeat Purchase Rate",
            "Customer Lifetime Value"
        ],
        "banking": [
            "Loan Approval Rate",
            "Average Balance",
            "Customer Retention",
            "Fraud Rate"
        ],
        "healthcare": [
            "Patient Count",
            "Average Treatment Cost",
            "Readmission Rate"
        ]
    }

    recommendations = kpis.get(domain, [
        "Record Count",
        "Growth Rate",
        "Average Value"
    ])

    return {
        "domain": domain,
        "available_columns": columns,
        "recommended_kpis": recommendations
    }


def generate_dashboard_layout(domain: str) -> Dict:
    """
    Generate a dashboard layout recommendation.
    """

    return {
        "dashboard_name": f"{domain.title()} Dashboard",
        "sections": [
            {
                "title": "Overview",
                "chart": "KPI Cards"
            },
            {
                "title": "Trend Analysis",
                "chart": "Line Chart"
            },
            {
                "title": "Category Distribution",
                "chart": "Bar Chart"
            },
            {
                "title": "Geographical Insights",
                "chart": "Map"
            },
            {
                "title": "Detailed Records",
                "chart": "Table"
            }
        ]
    }


def validate_sql_safety(query: str) -> Dict:
    """
    Validate whether a SQL query is safe.
    """

    query_upper = query.upper()

    blocked = [
        "DELETE",
        "DROP",
        "UPDATE",
        "ALTER",
        "INSERT",
        "TRUNCATE",
        "MERGE",
        "CREATE"
    ]

    warnings = []

    if not query_upper.strip().startswith("SELECT"):
        return {
            "safe": False,
            "reason": "Only SELECT queries are allowed."
        }

    for keyword in blocked:
        if keyword in query_upper:
            return {
                "safe": False,
                "reason": f"{keyword} statements are blocked."
            }

    if "SELECT *" in query_upper:
        warnings.append("Avoid using SELECT *.")

    if "LIMIT" not in query_upper:
        warnings.append("Consider adding LIMIT.")

    date_keywords = [
        "DATE",
        "ORDER_DATE",
        "EVENT_DATE",
        "TIMESTAMP"
    ]

    if not any(word in query_upper for word in date_keywords):
        warnings.append("No date filter detected.")

    return {
        "safe": True,
        "warnings": warnings
    }


def explain_query_result(metric: str,
                         trend: str,
                         change_percent: float) -> str:
    """
    Convert numeric results into business language.
    """

    if trend.lower() == "increasing":
        direction = "increased"

    elif trend.lower() == "decreasing":
        direction = "decreased"

    else:
        direction = "changed"

    return (
        f"{metric.replace('_',' ').title()} "
        f"has {direction} by {abs(change_percent)}%. "
        "Business users should investigate the key drivers "
        "behind this trend and compare it with previous periods."
    )