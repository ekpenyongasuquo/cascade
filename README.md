# CASCADE — Blast Radius Intelligence Agent

> Built for the **Build with DataHub: The Agent Hackathon**

**CASCADE** is a three-agent AI system that intercepts GitHub PR schema changes, traverses DataHub's full downstream lineage graph, assigns a financial cost to the breakage, auto-patches safe assets, and posts a complete incident report — all before a single line reaches production.

## 🚨 The Problem

A senior engineer renames a column in a source table. Three days later:
- 17 downstream dbt models are broken
- 2 ML models are serving stale features
- 1 revenue dashboard shows wrong numbers
- 1 compliance report filed incorrect figures to regulators

**Cost: $80,000+ in engineering time and regulatory exposure.**

This happens every week at every data-mature company. DataHub has the lineage graph to prevent it. CASCADE acts on it — proactively, autonomously, and with financial quantification.

## ✅ Live Demo

**API:** https://cascade-ca0h.onrender.com

**Trigger CASCADE manually:**
```bash
curl -X POST https://cascade-ca0h.onrender.com/trigger \
  -H "Content-Type: application/json" \
  -d '{"changed_field": "order_date", "new_field": "created_at"}'
```

**API Docs:** https://cascade-ca0h.onrender.com/docs

## 🏗️ Architecture