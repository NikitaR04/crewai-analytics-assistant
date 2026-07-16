def mcp_generate_report_markdown(
    profile,
    quality,
    kpis,
    ml
):

    report = f"""
# Dataset Summary

Rows: {profile['rows']}

Columns: {profile['columns']}

# Data Quality

{quality}

# Recommended KPIs

{kpis}

# ML Use Cases

{ml}

# Next Steps

- Build Dashboard

- Train ML Model

- Deploy Pipeline
"""

    return report