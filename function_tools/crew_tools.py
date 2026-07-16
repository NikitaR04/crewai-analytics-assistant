from typing import List

import pandas as pd
from crewai.tools import tool

# ======================================================
# Supervisor Tools
# ======================================================

from function_tools.supervisor_tools import (
    classify_user_request,
    create_agent_work_plan,
    summarize_chat_history,
    validate_final_response_structure,
    estimate_context_usage,
)

# ======================================================
# Analyst Tools
# ======================================================

from function_tools.analyst_tools import (
    profile_dataframe,
    suggest_kpi_metrics,
    generate_dashboard_layout,
    validate_sql_safety,
    explain_query_result,
)

# ======================================================
# Scientist Tools
# ======================================================

from function_tools.scientist_tools import (
    recommend_ml_problem_type,
    suggest_feature_engineering,
    detect_ml_data_risks,
    recommend_evaluation_metrics,
    create_ml_pipeline_plan,
)

# ======================================================
# Supervisor Tools
# ======================================================

@tool("Classify User Request")
def classify_user_request_tool(user_request: str):
    """Classify a user request."""
    return classify_user_request(user_request)


@tool("Create Agent Work Plan")
def create_agent_work_plan_tool(intent: str):
    """Create a work plan for the agents."""
    return create_agent_work_plan(intent)


@tool("Summarize Chat History")
def summarize_chat_history_tool(history: List[str]):
    """Summarize previous conversation."""
    return summarize_chat_history(history)


@tool("Validate Final Response")
def validate_final_response_tool(response: str):
    """Validate the final response structure."""
    return validate_final_response_structure(response)


@tool("Estimate Context Usage")
def estimate_context_usage_tool(text: str):
    """Estimate token/context usage."""
    return estimate_context_usage(text)


# ======================================================
# Analyst Tools
# ======================================================

@tool("Profile CSV")
def profile_dataframe_tool(file_path: str):
    """
    Profile a CSV dataset.
    """
    return profile_dataframe(file_path)


@tool("Suggest KPI Metrics")
def suggest_kpi_metrics_tool(domain: str, columns: List[str]):
    """
    Recommend KPIs for a business domain.
    """
    return suggest_kpi_metrics(domain, columns)


@tool("Generate Dashboard Layout")
def generate_dashboard_layout_tool(domain: str):
    """
    Recommend dashboard sections.
    """
    return generate_dashboard_layout(domain)


@tool("Validate SQL")
def validate_sql_tool(query: str):
    """
    Validate a SQL query.
    """
    return validate_sql_safety(query)


@tool("Explain Query Result")
def explain_query_result_tool(
    metric: str,
    trend: str,
    change: float,
):
    """
    Explain SQL results in business language.
    """
    return explain_query_result(
        metric,
        trend,
        change,
    )


# ======================================================
# Scientist Tools
# ======================================================

@tool("Recommend ML Problem")
def recommend_ml_problem_type_tool(problem: str):
    """
    Recommend the ML problem type.
    """
    return recommend_ml_problem_type(problem)


@tool("Suggest Feature Engineering")
def suggest_feature_engineering_tool(columns: List[str]):
    """
    Suggest feature engineering ideas.
    """
    return suggest_feature_engineering(columns)


@tool("Detect ML Data Risks")
def detect_ml_data_risks_tool(file_path: str):
    """
    Detect ML-related data quality risks from a CSV file.
    """
    df = pd.read_csv(file_path)
    return detect_ml_data_risks(df)


@tool("Recommend Evaluation Metrics")
def recommend_evaluation_metrics_tool(problem_type: str):
    """
    Recommend ML evaluation metrics.
    """
    return recommend_evaluation_metrics(problem_type)


@tool("Create ML Pipeline")
def create_ml_pipeline_plan_tool():
    """
    Generate a standard ML pipeline.
    """
    return create_ml_pipeline_plan()