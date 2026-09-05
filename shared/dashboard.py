
from pathlib import Path
import json, html, base64

def build_dashboard(project_root, title, domain, method):
    root=Path(project_root); metrics=json.loads((root/'artifacts'/'metrics.json').read_text())
    details={}
    if (root/'artifacts'/'details.json').exists(): details=json.loads((root/'artifacts'/'details.json').read_text())
    img=''
    if (root/'artifacts'/'result.png').exists():
        b64=base64.b64encode((root/'artifacts'/'result.png').read_bytes()).decode(); img=f'<img src="data:image/png;base64,{b64}" alt="result chart">'
    cards=''.join(f'<div class="card"><b>{html.escape(str(k))}</b><span>{html.escape(str(v))}</span></div>' for k,v in metrics.items())
    phases=['Business Understanding','Data Understanding','Data Preparation','Modeling','Evaluation','Deployment / Communication']
    phase_html=''.join(f'<li><strong>{p}</strong><br><small>Documented and reproducible in this project.</small></li>' for p in phases)
    doc=f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>
    body{{font-family:Arial,sans-serif;background:#f6f7f9;color:#1c2430;margin:0}} main{{max-width:1050px;margin:36px auto;background:white;padding:34px;border-radius:14px;box-shadow:0 4px 20px #0001}} h1{{margin-bottom:4px}} .sub{{color:#667085}} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:24px 0}} .card{{border:1px solid #e2e6ea;border-radius:10px;padding:16px;display:flex;flex-direction:column;gap:7px}} .card span{{font-size:18px}} img{{max-width:100%;border:1px solid #e5e7eb;border-radius:10px}} ul{{line-height:1.6}} .note{{background:#f8fafc;padding:14px;border-left:4px solid #64748b}} code{{background:#f1f5f9;padding:2px 5px}}</style></head><body><main>
    <p class="sub">Student reproduction project · {html.escape(domain)}</p><h1>{html.escape(title)}</h1><p>{html.escape(method)}</p>
    <h2>Experiment results</h2><div class="grid">{cards}</div>{img}
    <h2>CRISP-DM walkthrough</h2><ul>{phase_html}</ul>
    <h2>Reproducibility and audit</h2><p class="note">Fixed random seed: <code>42</code>. Evaluation logic is in <code>src/experiment.py</code>. Generated metrics are stored in <code>artifacts/metrics.json</code>.</p>
    <h2>Additional details</h2><pre>{html.escape(json.dumps(details,indent=2)[:6000])}</pre>
    </main></body></html>"""
    (root/'dashboard.html').write_text(doc)
