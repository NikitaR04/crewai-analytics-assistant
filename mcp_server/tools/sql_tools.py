import re
from pathlib import Path
from typing import Dict

import duckdb


BLOCKED_COMMANDS = [
    "DELETE",
    "UPDATE",
    "DROP",
    "ALTER",
    "INSERT",
    "MERGE",
    "TRUNCATE",
    "CREATE"
]


def mcp_validate_sql(query: str) -> Dict:
    """
    Validate whether a SQL query is safe.
    """

    query_upper = query.upper()

    for cmd in BLOCKED_COMMANDS:
        if re.search(rf"\b{cmd}\b", query_upper):
            return {
                "safe": False,
                "reason": f"{cmd} statements are blocked."
            }

    warnings = []

    if "SELECT *" in query_upper:
        warnings.append("Avoid SELECT *")

    if "LIMIT" not in query_upper:
        warnings.append("Consider adding LIMIT")

    return {
        "safe": True,
        "warnings": warnings
    }


def mcp_run_duckdb_query(csv_path: str, query: str):
    """
    Execute a read-only DuckDB query on a CSV.
    """

    validation = mcp_validate_sql(query)

    if not validation["safe"]:
        raise ValueError(validation["reason"])

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(csv_path)

    con = duckdb.connect()

    con.execute(f"""
        CREATE VIEW dataset AS
        SELECT *
        FROM read_csv_auto('{path.as_posix()}')
    """)

    result = con.execute(query).fetchdf()

    con.close()

    return result.to_dict(orient="records")