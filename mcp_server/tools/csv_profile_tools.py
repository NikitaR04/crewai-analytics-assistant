from pathlib import Path
from typing import Dict

import pandas as pd


def mcp_profile_csv(file_path: str) -> Dict:
    """
    Profile a CSV file.

    Returns:
        - Row count
        - Column count
        - Data types
        - Missing values
        - Duplicate rows
        - Sample records
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    df = pd.read_csv(path)

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "data_types": {k: str(v) for k, v in df.dtypes.items()},
        "missing_values": df.isna().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "sample_rows": df.head(5).to_dict(orient="records"),
    }