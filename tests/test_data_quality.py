from mcp_server.tools.data_quality_tools import *

print(
    mcp_detect_data_quality_issues(
        "mcp_server/sample_data/customers_sample.csv"
    )
)