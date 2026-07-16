def mcp_generate_kpi_catalog(domain: str, columns):

    kpis = {

        "ecommerce": [

            {

                "name": "Total Revenue",

                "formula": "SUM(revenue)",

                "grain": "Daily"

            },

            {

                "name": "Average Order Value",

                "formula": "AVG(revenue)",

                "grain": "Daily"

            }

        ]

    }

    return {

        "domain": domain,

        "columns": columns,

        "kpis": kpis.get(domain, [])

    }