from mcp_server.tools.sql_tools import *

query = """
SELECT customer_id,revenue
FROM dataset
LIMIT 5
"""

print(mcp_validate_sql(query))

print()

print(
    mcp_run_duckdb_query(
        "mcp_server/sample_data/customers_sample.csv",
        query
    )
)