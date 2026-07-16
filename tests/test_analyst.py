from function_tools.analyst_tools import *

import pandas as pd

df = pd.DataFrame({
    "customer_id":[1,2,3,3],
    "revenue":[100,200,None,150],
    "country":["IN","US","UK","UK"]
})

print("\nPROFILE")
print(profile_dataframe(df))

print("\nKPIs")
print(
    suggest_kpi_metrics(
        "ecommerce",
        list(df.columns)
    )
)

print("\nDashboard")
print(
    generate_dashboard_layout(
        "ecommerce"
    )
)

print("\nSQL")
print(
    validate_sql_safety(
        "SELECT * FROM sales"
    )
)

print("\nExplanation")
print(
    explain_query_result(
        "monthly_revenue",
        "decreasing",
        -12.5
    )
)