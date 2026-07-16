from mcp_server.tools.csv_profile_tools import mcp_profile_csv

result = mcp_profile_csv(
    "mcp_server/sample_data/customers_sample.csv"
)

print(result)