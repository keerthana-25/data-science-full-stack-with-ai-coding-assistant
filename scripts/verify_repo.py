from pathlib import Path
repo=Path(__file__).resolve().parents[1]
rows=[]
required=['README.md','prompts.md','abstract.md','paper.md','article.md','IMPLEMENTATION_PLAN.md','AUDIT_REPORT.md','skills/SKILL.md','src/experiment.py','dashboard.html','artifacts/metrics.json','artifacts/result.png','docs/screenshots/dashboard_01.png','docs/screenshots/dashboard_02.png']
for p in sorted(repo.glob('[0-9][0-9]_*')):
    miss=[f for f in required if not (p/f).exists()]
    rows.append((p.name,not miss,miss))
lines=['# Verification Report','','This report checks the generated submission artifacts after execution.','', '| Project | Status | Missing |','|---|---|---|']
for name,ok,miss in rows:
    lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {', '.join(miss) if miss else '-'} |")
lines += ['', f"Overall: **{'PASS' if all(x[1] for x in rows) else 'FAIL'}** ({sum(x[1] for x in rows)}/{len(rows)} projects complete)"]
(repo/'VERIFICATION.md').write_text('\n'.join(lines)+'\n')
print(lines[-1])
