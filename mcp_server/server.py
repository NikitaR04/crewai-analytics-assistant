from mcp.server.fastmcp import FastMCP

from mcp_server.tools.csv_profile_tools import mcp_profile_csv
from mcp_server.tools.sql_tools import (
    mcp_validate_sql,
    mcp_run_duckdb_query,
)
from mcp_server.tools.data_quality_tools import (
    mcp_detect_data_quality_issues,
)
from mcp_server.tools.kpi_tools import (
    mcp_generate_kpi_catalog,
)
from mcp_server.tools.ml_tools import (
    mcp_recommend_ml_use_cases,
)
from mcp_server.tools.report_tools import (
    mcp_generate_report_markdown,
)

# ----------------------------------------------------
# Create MCP Server
# ----------------------------------------------------

mcp = FastMCP("analytics_mcp_server")


# ----------------------------------------------------
# Health Check
# ----------------------------------------------------

@mcp.tool()
def hello():
    """
    Test whether the MCP server is running.
    """
    return {
        "status": "success",
        "message": "Analytics MCP Server is running!"
    }


# ----------------------------------------------------
# CSV Profiling
# ----------------------------------------------------

@mcp.tool()
def profile_csv(file_path: str):
    return mcp_profile_csv(file_path)


# ----------------------------------------------------
# SQL Validation
# ----------------------------------------------------

@mcp.tool()
def validate_sql(query: str):
    return mcp_validate_sql(query)


# ----------------------------------------------------
# DuckDB Query Execution
# ----------------------------------------------------

@mcp.tool()
def run_duckdb_query(file_path: str, query: str):
    return mcp_run_duckdb_query(file_path, query)


# ----------------------------------------------------
# Data Quality
# ----------------------------------------------------

@mcp.tool()
def detect_data_quality(file_path: str):
    return mcp_detect_data_quality_issues(file_path)


# ----------------------------------------------------
# KPI Catalog
# ----------------------------------------------------

@mcp.tool()
def generate_kpi_catalog(domain: str, columns: list):
    return mcp_generate_kpi_catalog(domain, columns)


# ----------------------------------------------------
# ML Use Cases
# ----------------------------------------------------

@mcp.tool()
def recommend_ml_use_cases(columns: list):
    return mcp_recommend_ml_use_cases(columns)


# ----------------------------------------------------
# Markdown Report
# ----------------------------------------------------

@mcp.tool()
def generate_report(profile, quality, kpis, ml):
    return mcp_generate_report_markdown(
        profile,
        quality,
        kpis,
        ml,
    )


# ----------------------------------------------------
# Run Server
# ----------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Analytics MCP Server")
    print("Server Name : analytics_mcp_server")
    print("Available Tools")
    print("- hello")
    print("- profile_csv")
    print("- validate_sql")
    print("- run_duckdb_query")
    print("- detect_data_quality")
    print("- generate_kpi_catalog")
    print("- recommend_ml_use_cases")
    print("- generate_report")
    print("=" * 60)

    mcp.run()