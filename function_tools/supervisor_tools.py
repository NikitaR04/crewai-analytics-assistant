import math
import re
from typing import Dict, List


def classify_user_request(user_request: str) -> Dict:
    """
    Classify the user's request and recommend the appropriate agent.
    """

    text = user_request.lower()

    analyst_keywords = [
        "dashboard", "kpi", "sql", "analytics",
        "report", "chart", "business"
    ]

    scientist_keywords = [
        "machine learning", "ml", "prediction",
        "forecast", "classification",
        "regression", "clustering",
        "feature engineering", "model"
    ]

    analyst_score = sum(word in text for word in analyst_keywords)
    scientist_score = sum(word in text for word in scientist_keywords)

    if analyst_score > 0 and scientist_score > 0:
        return {
            "intent": "mixed",
            "recommended_agent": "Both",
            "reason": "Request contains analytics and ML tasks."
        }

    if analyst_score:
        return {
            "intent": "analytics",
            "recommended_agent": "Data Analyst Agent",
            "reason": "Business analytics related request."
        }

    if scientist_score:
        return {
            "intent": "data_science",
            "recommended_agent": "Data Scientist Agent",
            "reason": "Machine learning related request."
        }

    return {
        "intent": "general",
        "recommended_agent": "Supervisor Agent",
        "reason": "General request."
    }


def create_agent_work_plan(intent: str) -> Dict:
    """
    Create a work plan for agents.
    """

    plans = {
        "analytics": [
            "Profile dataset",
            "Generate KPI suggestions",
            "Recommend dashboards",
            "Summarize insights"
        ],

        "data_science": [
            "Analyze dataset",
            "Suggest ML problem",
            "Recommend features",
            "Suggest evaluation metrics"
        ],

        "mixed": [
            "Profile dataset",
            "Generate KPIs",
            "Detect data quality issues",
            "Recommend ML use cases",
            "Combine results"
        ]
    }

    return {
        "steps": plans.get(intent, ["Analyze request"])
    }


def summarize_chat_history(chat_history: List[str]) -> str:
    """
    Return a short summary of previous messages.
    """

    if not chat_history:
        return "No previous conversation."

    combined = " ".join(chat_history)

    words = combined.split()

    return " ".join(words[:60])


def validate_final_response_structure(response: str) -> Dict:

    required_sections = [

        "Direct Answer",

        "Dataset Summary",

        "Data Quality",

        "Recommended KPIs",

        "ML Use Cases",

        "Next Steps"

    ]

    missing = []

    for section in required_sections:

        if section.lower() not in response.lower():

            missing.append(section)

    return {

        "is_valid": len(missing) == 0,

        "missing_sections": missing

    }


def estimate_context_usage(text: str, context_window: int = 8192) -> Dict:

    estimated_tokens = math.ceil(len(text) / 4)

    usage = round((estimated_tokens / context_window) * 100, 2)

    return {

        "estimated_input_tokens": estimated_tokens,

        "context_window": context_window,

        "usage_percent": usage

    }