"""
SCOUT Agent — Lineage Traversal
Discovers all downstream assets affected by a schema change.
"""

import os
from typing import Any
from dotenv import load_dotenv

load_dotenv()

DATAHUB_SERVER = os.getenv("DATAHUB_SERVER", "http://127.0.0.1:8979")


def run_scout(entity_urn: str) -> dict[str, Any]:
    """
    Given a changed entity URN, traverse downstream lineage
    and return all affected assets.
    """
    print(f"\n[SCOUT] Activating for entity: {entity_urn}")

    # --- MOCK MODE (until real DataHub token arrives) ---
    # Replace this block with real get_lineage() call once token is available
    mock_lineage = {
        "source_urn": entity_urn,
        "affected_assets": [
            {
                "urn": "urn:li:dataset:(urn:li:dataPlatform:snowflake,analytics.revenue_forecast,PROD)",
                "name": "revenue_forecast",
                "platform": "snowflake",
                "domain": "finance",
                "tags": ["revenue_critical"],
            },
            {
                "urn": "urn:li:dataset:(urn:li:dataPlatform:snowflake,ml.churn_prediction,PROD)",
                "name": "churn_prediction",
                "platform": "snowflake",
                "domain": "ml_platform",
                "tags": ["revenue_critical"],
            },
            {
                "urn": "urn:li:dataset:(urn:li:dataPlatform:snowflake,reporting.q2_compliance,PROD)",
                "name": "q2_compliance_report",
                "platform": "snowflake",
                "domain": "legal",
                "tags": ["regulatory"],
            },
            {
                "urn": "urn:li:dataset:(urn:li:dataPlatform:snowflake,marketing.attribution,PROD)",
                "name": "marketing_attribution",
                "platform": "snowflake",
                "domain": "marketing",
                "tags": ["business_critical"],
            },
        ],
        "total_affected": 4,
        "max_hops": 3,
    }

    print(f"[SCOUT] Found {mock_lineage['total_affected']} affected assets")
    for asset in mock_lineage["affected_assets"]:
        print(f"  → {asset['name']} [{', '.join(asset['tags'])}]")

    return mock_lineage


if __name__ == "__main__":
    # Test SCOUT directly
    test_urn = "urn:li:dataset:(urn:li:dataPlatform:postgres,ecommerce.orders,PROD)"
    result = run_scout(test_urn)
    print(f"\n[SCOUT] Complete. Total affected: {result['total_affected']}")