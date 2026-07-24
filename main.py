"""
CASCADE — Blast Radius Intelligence Agent
Main orchestrator — wires SCOUT → VALUATION → PATCH
"""

from agents.scout import run_scout
from agents.valuation import run_valuation
from agents.patch import run_patch


def run_cascade(entity_urn: str, changed_field: str, new_field: str) -> dict:
    print("\n" + "="*50)
    print("  CASCADE — BLAST RADIUS INTELLIGENCE AGENT")
    print("="*50)

    # Stage 1 — SCOUT
    scout_result = run_scout(entity_urn)

    # Stage 2 — VALUATION
    valuation_result = run_valuation(scout_result)

    # Stage 3 — PATCH
    patch_result = run_patch(valuation_result, changed_field, new_field)

    print("\n" + "="*50)
    print("  CASCADE COMPLETE")
    print(f"  Assets affected:  {valuation_result['total_affected']}")
    print(f"  Auto-patched:     {patch_result['total_auto_patched']}")
    print(f"  Needs review:     {patch_result['total_needs_review']}")
    print(f"  Total cost risk:  ${valuation_result['total_estimated_cost']:,}")
    print(f"  Overall risk:     {valuation_result['overall_risk']}")
    print("="*50)

    return {
        "scout": scout_result,
        "valuation": valuation_result,
        "patch": patch_result,
    }


if __name__ == "__main__":
    run_cascade(
        entity_urn="urn:li:dataset:(urn:li:dataPlatform:postgres,ecommerce.orders,PROD)",
        changed_field="order_date",
        new_field="created_at",
    )
