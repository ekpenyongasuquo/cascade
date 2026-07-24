"""
VALUATION Agent — Blast Radius Financial Quantification
Reads tags and domain from each affected asset and assigns a cost estimate.
"""

import os
from typing import Any
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Cost multipliers by tag
COST_TABLE = {
    "revenue_critical": 18000,
    "regulatory": 35000,
    "business_critical": 9000,
    "pii": 12000,
    "default": 3000,
}


def calculate_cost(tags: list[str]) -> int:
    for tag in tags:
        if tag in COST_TABLE:
            return COST_TABLE[tag]
    return COST_TABLE["default"]


def run_valuation(scout_result: dict[str, Any]) -> dict[str, Any]:
    """
    Takes SCOUT output and produces a financial blast radius report.
    """
    print(f"\n[VALUATION] Analyzing {scout_result['total_affected']} affected assets...")

    assets = scout_result["affected_assets"]
    valued_assets = []
    total_cost = 0
    has_regulatory = False
    has_revenue_critical = False

    for asset in assets:
        cost = calculate_cost(asset["tags"])
        total_cost += cost
        is_regulatory = "regulatory" in asset["tags"]
        is_revenue = "revenue_critical" in asset["tags"]

        if is_regulatory:
            has_regulatory = True
        if is_revenue:
            has_revenue_critical = True

        valued_assets.append({
            **asset,
            "estimated_cost": cost,
            "risk_level": "CRITICAL" if is_regulatory else "HIGH" if is_revenue else "MEDIUM",
            "requires_human_review": is_regulatory,
        })

        print(f"  → {asset['name']}: ${cost:,} [{valued_assets[-1]['risk_level']}]")

    # Use Groq to generate a human-readable summary
    client = Groq(api_key=GROQ_API_KEY)
    asset_summary = "\n".join([
        f"- {a['name']} (tags: {', '.join(a['tags'])}, cost: ${a['estimated_cost']:,}, risk: {a['risk_level']})"
        for a in valued_assets
    ])

    prompt = f"""You are CASCADE, a data pipeline impact analyst.
A schema change has affected {scout_result['total_affected']} downstream assets.
Total estimated remediation cost: ${total_cost:,}

Affected assets:
{asset_summary}

Write a concise 3-sentence executive summary of the blast radius impact.
Focus on financial risk, regulatory exposure, and urgency.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )

    summary = response.choices[0].message.content.strip()

    report = {
        "source_urn": scout_result["source_urn"],
        "total_affected": scout_result["total_affected"],
        "total_estimated_cost": total_cost,
        "has_regulatory": has_regulatory,
        "has_revenue_critical": has_revenue_critical,
        "overall_risk": "CRITICAL" if has_regulatory else "HIGH" if has_revenue_critical else "MEDIUM",
        "valued_assets": valued_assets,
        "executive_summary": summary,
    }

    print(f"\n[VALUATION] Total blast radius cost: ${total_cost:,}")
    print(f"[VALUATION] Overall risk: {report['overall_risk']}")
    print(f"[VALUATION] Executive summary:\n{summary}")

    return report


if __name__ == "__main__":
    # Test VALUATION with mock SCOUT output
    mock_scout = {
        "source_urn": "urn:li:dataset:(urn:li:dataPlatform:postgres,ecommerce.orders,PROD)",
        "affected_assets": [
            {"urn": "urn:li:dataset:(snowflake,analytics.revenue_forecast,PROD)", "name": "revenue_forecast", "platform": "snowflake", "domain": "finance", "tags": ["revenue_critical"]},
            {"urn": "urn:li:dataset:(snowflake,ml.churn_prediction,PROD)", "name": "churn_prediction", "platform": "snowflake", "domain": "ml_platform", "tags": ["revenue_critical"]},
            {"urn": "urn:li:dataset:(snowflake,reporting.q2_compliance,PROD)", "name": "q2_compliance_report", "platform": "snowflake", "domain": "legal", "tags": ["regulatory"]},
            {"urn": "urn:li:dataset:(snowflake,marketing.attribution,PROD)", "name": "marketing_attribution", "platform": "snowflake", "domain": "marketing", "tags": ["business_critical"]},
        ],
        "total_affected": 4,
        "max_hops": 3,
    }

    result = run_valuation(mock_scout)
    print(f"\n[VALUATION] Complete.")