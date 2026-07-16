def mcp_recommend_ml_use_cases(columns):

    use_cases = []

    if "customer_id" in columns:

        use_cases.append({

            "use_case": "Customer Churn Prediction",

            "problem_type": "Classification"

        })

    if "revenue" in columns:

        use_cases.append({

            "use_case": "Revenue Forecasting",

            "problem_type": "Forecasting"

        })

    return {

        "ml_use_cases": use_cases

    }