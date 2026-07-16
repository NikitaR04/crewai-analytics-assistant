from function_tools.supervisor_tools import *

print(classify_user_request(
    "Analyze the sales dataset and recommend KPIs"
))

print()

print(create_agent_work_plan("mixed"))

print()

print(
    summarize_chat_history(
        [
            "Hello",
            "Analyze revenue",
            "Suggest ML model"
        ]
    )
)

print()

print(
    estimate_context_usage(
        "Hello " * 100
    )
)