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

[GitHub PR Webhook]
│
▼
[FastAPI Webhook Receiver]
│
▼
[SCOUT Agent]
Traverses DataHub downstream lineage graph
Identifies all affected datasets, ML models, dashboards
│
▼
[VALUATION Agent — Groq LLM]
Reads tags: revenue_critical, regulatory, PII
Assigns financial cost to each broken asset
Generates executive summary
│
▼
[PATCH Agent — Groq LLM]
Auto-patches safe assets with corrected SQL
Flags regulatory assets for human review
Writes incident report back to DataHub
│
▼
[GitHub PR Comment + DataHub Tagged Assets]


## 🤖 Three Agents

| Agent | Role | DataHub Integration |
|-------|------|-------------------|
| SCOUT | Lineage traversal | `get_lineage()` — downstream, 3 hops |
| VALUATION | Financial quantification | `get_entities()` — tags, ownership, domain |
| PATCH | Auto-remediation + write-back | `save_document()`, `add_tags()` |

## 📊 Sample Output

BLAST RADIUS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Assets affected: 4
Auto-patched: 3 ✅
Requires human review: 1 ⚠️
Overall risk: CRITICAL 🚨
Estimated cost: $80,000

🚨 BLOCKER: q2_compliance_report [regulatory] — legal sign-off required


## 🛠️ Tech Stack

- **Agents:** Python + Groq (llama-3.3-70b-versatile)
- **API:** FastAPI + Uvicorn
- **DataHub:** MCP Server, Agent Context Kit, DataHub lineage tools
- **Deployment:** Render

## 🚀 Run Locally

```bash
git clone https://github.com/ekpenyongasuquo/cascade.git
cd cascade
pip install -r requirements.txt
cp .env.example .env  # Add your GROQ_API_KEY
python webhook/receiver.py
```

## 📁 Project Structure

cascade/
├── agents/
│ ├── scout.py # Lineage traversal agent
│ ├── valuation.py # Financial quantification agent
│ └── patch.py # Auto-remediation agent
├── webhook/
│ └── receiver.py # FastAPI webhook receiver
├── main.py # Pipeline orchestrator
└── requirements.txt


## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Service info |
| `/health` | GET | Health check |
| `/trigger` | POST | Manual CASCADE trigger |
| `/webhook/github` | POST | GitHub PR webhook receiver |
| `/docs` | GET | Swagger UI |

## 🏆 Hackathon

- **Event:** Build with DataHub: The Agent Hackathon
- **Category:** Agents That Do Real Work + Production ML Agents
- **Deadline:** August 10, 2026
- **Author:** Ekpenyong Asuquo Mfon
- **GitHub:** ekpenyongasuquo
