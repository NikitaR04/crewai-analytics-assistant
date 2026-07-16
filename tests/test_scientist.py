from function_tools.scientist_tools import *

import pandas as pd

df = pd.DataFrame({

    "customer_id":[1,2,3,3],

    "revenue":[100,200,None,150],

    "country":["IN","US","UK","UK"]

})

print(recommend_ml_problem_type(
    "Predict customer churn"
))

print()

print(
    suggest_feature_engineering(
        list(df.columns)
    )
)

print()

print(
    detect_ml_data_risks(df)
)

print()

print(
    recommend_evaluation_metrics(
        "classification"
    )
)

print()

print(
    create_ml_pipeline_plan()
)