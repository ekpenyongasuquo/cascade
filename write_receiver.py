content = open('webhook/receiver.py', 'w', encoding='utf-8')
content.write("""import hashlib, hmac, os, json
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.scout import run_scout
from agents.valuation import run_valuation
from agents.patch import run_patch
load_dotenv()
app = FastAPI(title="CASCADE", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
def run_cascade_pipeline(sc):
    s = run_scout(sc["entity_urn"])
    v = run_valuation(s)
    p = run_patch(v, sc["changed_field"], sc["new_field"])
    return {"scout": s, "valuation": v, "patch": p}
@app.get("/")
async def root():
    d = Path(__file__).parent.parent / "dashboard.html"
    if d.exists():
        return HTMLResponse(content=d.read_text(encoding="utf-8"))
    return JSONResponse({"name": "CASCADE", "status": "running"})
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.post("/trigger")
async def trigger(request: Request):
    body = await request.json()
    sc = {"entity_urn": body.get("entity_urn", "urn:li:dataset:(urn:li:dataPlatform:postgres,ecommerce.orders,PROD)"), "changed_field": body.get("changed_field", "order_date"), "new_field": body.get("new_field", "created_at"), "pr_number": "DEMO", "pr_title": "demo", "repo": "demo/ecommerce"}
    r = run_cascade_pipeline(sc)
    return JSONResponse({"status": "cascade_complete", "schema_change": sc, "blast_radius": {"total_affected": r["valuation"]["total_affected"], "total_cost": r["valuation"]["total_estimated_cost"], "overall_risk": r["valuation"]["overall_risk"], "auto_patched": r["patch"]["total_auto_patched"], "needs_review": r["patch"]["total_needs_review"]}, "incident_report": r["patch"]["incident_report"]})
@app.post("/webhook/github")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    return JSONResponse({"status": "received"})
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
""")
content.close()
print("receiver.py written successfully")