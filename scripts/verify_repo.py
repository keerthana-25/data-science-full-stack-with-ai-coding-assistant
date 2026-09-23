from pathlib import Path
repo = Path(__file__).resolve().parents[1]
required = ['README.md', 'prompts.md', 'src/experiment.py', 'dashboard.html',
            'artifacts/metrics.json', 'artifacts/result.png',
            'docs/screenshots/dashboard_01.png', 'docs/screenshots/dashboard_02.png']
ok = True
for p in sorted(repo.glob('[0-9][0-9]_*')):
    missing = [f for f in required if not (p / f).exists()]
    if missing:
        ok = False
        print(f"FAIL {p.name}: missing {', '.join(missing)}")
    else:
        print(f"PASS {p.name}")
print('All projects complete' if ok else 'Some projects are missing files')
