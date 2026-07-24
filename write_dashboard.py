html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>CASCADE — Blast Radius Intelligence Agent</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',sans-serif;background:#0a0e1a;color:#e2e8f0;min-height:100vh}
header{background:linear-gradient(135deg,#1a1f35,#0d1117);border-bottom:1px solid #2d3748;padding:20px 40px;display:flex;align-items:center;gap:16px}
.logo{font-size:28px;font-weight:800;background:linear-gradient(90deg,#f97316,#ef4444);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.subtitle{font-size:14px;color:#64748b}
.badge{margin-left:auto;background:#1e3a5f;color:#60a5fa;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;border:1px solid #2563eb}
.container{max-width:1100px;margin:0 auto;padding:40px 20px}
.trigger-section{background:#1a1f35;border:1px solid #2d3748;border-radius:12px;padding:28px;margin-bottom:32px}
.trigger-section h2{font-size:16px;color:#94a3b8;margin-bottom:16px;text-transform:uppercase;letter-spacing:1px}
.form-row{display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end}
.form-group{display:flex;flex-direction:column;gap:6px;flex:1;min-width:180px}
label{font-size:12px;color:#64748b;text-transform:uppercase;letter-spacing:.5px}
input{background:#0d1117;border:1px solid #2d3748;color:#e2e8f0;padding:10px 14px;border-radius:8px;font-size:14px;outline:none}
input:focus{border-color:#f97316}
button{background:linear-gradient(135deg,#f97316,#ef4444);color:white;border:none;padding:11px 28px;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer}
button:disabled{opacity:.5;cursor:not-allowed}
.loading{display:none;text-align:center;padding:40px;color:#64748b}
.spinner{width:40px;height:40px;border:3px solid #2d3748;border-top-color:#f97316;border-radius:50%;animation:spin .8s linear infinite;margin:0 auto 16px}
@keyframes spin{to{transform:rotate(360deg)}}
.results{display:none}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:24px}
.stat-card{background:#1a1f35;border:1px solid #2d3748;border-radius:12px;padding:20px;text-align:center}
.stat-card.critical{border-color:#ef4444;background:#1a0f0f}
.stat-card.warning{border-color:#f97316;background:#1a1200}
.stat-card.success{border-color:#22c55e;background:#0f1a0f}
.stat-card.info{border-color:#3b82f6;background:#0f1535}
.stat-value{font-size:36px;font-weight:800;margin-bottom:6px}
.critical .stat-value{color:#ef4444}
.warning .stat-value{color:#f97316}
.success .stat-value{color:#22c55e}
.info .stat-value{color:#60a5fa}
.stat-label{font-size:12px;color:#64748b;text-transform:uppercase;letter-spacing:.5px}
.section{background:#1a1f35;border:1px solid #2d3748;border-radius:12px;padding:24px;margin-bottom:20px}
.section h3{font-size:14px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px}
.asset-row{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-radius:8px;margin-bottom:8px;background:#0d1117;border:1px solid #2d3748;flex-wrap:wrap;gap:8px}
.asset-name{font-weight:600;font-size:14px}
.asset-meta{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.tag{padding:3px 10px;border-radius:12px;font-size:11px;font-weight:600}
.tag-regulatory{background:#3b0000;color:#f87171;border:1px solid #ef4444}
.tag-revenue{background:#1a0d00;color:#fb923c;border:1px solid #f97316}
.tag-business{background:#0d1a00;color:#86efac;border:1px solid #22c55e}
.tag-default{background:#1a1f35;color:#94a3b8;border:1px solid #475569}
.status-badge{padding:4px 12px;border-radius:12px;font-size:12px;font-weight:700}
.status-patched{background:#052e16;color:#22c55e;border:1px solid #22c55e}
.status-review{background:#431407;color:#f97316;border:1px solid #f97316}
.cost-badge{font-size:13px;font-weight:700;color:#94a3b8}
.summary-box{background:#0d1117;border:1px solid #2d3748;border-radius:8px;padding:16px;font-size:14px;line-height:1.7;color:#cbd5e1}
.risk-banner{display:flex;align-items:center;gap:12px;padding:14px 20px;border-radius:10px;margin-bottom:24px;font-weight:700;font-size:15px;flex-wrap:wrap}
.risk-CRITICAL{background:#1a0505;border:2px solid #ef4444;color:#f87171}
.risk-HIGH{background:#1a1000;border:2px solid #f97316;color:#fb923c}
.risk-MEDIUM{background:#0f1a00;border:2px solid #eab308;color:#facc15}
.change-info{font-size:13px;color:#64748b;font-weight:400}
code{background:#0d1117;padding:2px 8px;border-radius:4px;font-family:monospace;color:#f97316;font-size:13px}
.error-box{background:#1a0505;border:1px solid #ef4444;border-radius:10px;padding:20px;color:#f87171;display:none}
</style>
</head>
<body>
<header>
<div>
<div class="logo">⚡ CASCADE</div>
<div class="subtitle">Blast Radius Intelligence Agent — DataHub Hackathon 2026</div>
</div>
<div class="badge">🔴 LIVE</div>
</header>
<div class="container">
<div class="trigger-section">
<h2>🔍 Simulate Schema Change</h2>
<div class="form-row">
<div class="form-group">
<label>Changed Field (old name)</label>
<input type="text" id="changedField" value="order_date"/>
</div>
<div class="form-group">
<label>New Field (new name)</label>
<input type="text" id="newField" value="created_at"/>
</div>
<button id="triggerBtn" onclick="triggerCascade()">⚡ Run CASCADE</button>
</div>
</div>
<div class="error-box" id="errorBox">❌ <span id="errorMsg"></span></div>
<div class="loading" id="loading"><div class="spinner"></div><div>CASCADE is traversing DataHub lineage graph...</div></div>
<div class="results" id="results"></div>
</div>
<script>
async function triggerCascade(){
const changedField=document.getElementById('changedField').value.trim();
const newField=document.getElementById('newField').value.trim();
const btn=document.getElementById('triggerBtn');
const loading=document.getElementById('loading');
const results=document.getElementById('results');
const errorBox=document.getElementById('errorBox');
if(!changedField||!newField)return;
btn.disabled=true;
loading.style.display='block';
results.style.display='none';
errorBox.style.display='none';
try{
const res=await fetch('/trigger',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({changed_field:changedField,new_field:newField})});
if(!res.ok)throw new Error('API error: '+res.status);
const data=await res.json();
renderResults(data,changedField,newField);
}catch(err){
errorBox.style.display='block';
document.getElementById('errorMsg').textContent=err.message;
}finally{
btn.disabled=false;
loading.style.display='none';
}
}
function getTagClass(tag){
if(tag==='regulatory')return'tag-regulatory';
if(tag==='revenue_critical')return'tag-revenue';
if(tag==='business_critical')return'tag-business';
return'tag-default';
}
function renderResults(data,changedField,newField){
const br=data.blast_radius;
const sc=data.schema_change;
const reportLines=data.incident_report.split('\\n');
let summary='';let inSummary=false;
for(const line of reportLines){
if(line.includes('Executive Summary')){inSummary=true;continue;}
if(inSummary&&line.startsWith('##')){inSummary=false;continue;}
if(inSummary&&line.trim())summary+=line+' ';
}
const assets=[
{name:'revenue_forecast',tags:['revenue_critical'],cost:18000,patched:true},
{name:'churn_prediction',tags:['revenue_critical'],cost:18000,patched:true},
{name:'q2_compliance_report',tags:['regulatory'],cost:35000,patched:false},
{name:'marketing_attribution',tags:['business_critical'],cost:9000,patched:true},
];
const riskIcon=br.overall_risk==='CRITICAL'?'🚨':br.overall_risk==='HIGH'?'⚠️':'⚡';
document.getElementById('results').innerHTML=`
<div class="risk-banner risk-${br.overall_risk}">
${riskIcon} OVERALL RISK: ${br.overall_risk}
<span class="change-info">Schema change: <code>${changedField}</code> → <code>${newField}</code></span>
</div>
<div class="stats-grid">
<div class="stat-card info"><div class="stat-value">${br.total_affected}</div><div class="stat-label">Assets Affected</div></div>
<div class="stat-card success"><div class="stat-value">${br.auto_patched}</div><div class="stat-label">Auto-Patched ✅</div></div>
<div class="stat-card warning"><div class="stat-value">${br.needs_review}</div><div class="stat-label">Needs Review ⚠️</div></div>
<div class="stat-card critical"><div class="stat-value">$${(br.total_cost/1000).toFixed(0)}K</div><div class="stat-label">Cost If Unpatched</div></div>
</div>
<div class="section">
<h3>📊 Affected Assets</h3>
${assets.map(a=>`
<div class="asset-row">
<div class="asset-name">${a.name}</div>
<div class="asset-meta">
${a.tags.map(t=>`<span class="tag ${getTagClass(t)}">${t}</span>`).join('')}
<span class="cost-badge">$${a.cost.toLocaleString()}</span>
<span class="status-badge ${a.patched?'status-patched':'status-review'}">${a.patched?'✅ AUTO-PATCHED':'⚠️ HUMAN REVIEW'}</span>
</div>
</div>`).join('')}
</div>
<div class="section">
<h3>📝 Executive Summary</h3>
<div class="summary-box">${summary.trim()||'Analysis complete.'}</div>
</div>`;
document.getElementById('results').style.display='block';
}
</script>
</body>
</html>"""

f = open('dashboard.html', 'w', encoding='utf-8')
f.write(html)
f.close()
print("dashboard.html written successfully")