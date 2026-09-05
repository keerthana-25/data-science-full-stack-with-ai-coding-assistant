
from pathlib import Path
import subprocess, tempfile, sys, shutil
repo=Path(__file__).resolve().parents[1]
failed=[]
for p in sorted(repo.glob('[0-9][0-9]_*')):
    html=p/'dashboard.html'; outdir=p/'docs'/'screenshots'
    if not html.exists(): failed.append(p.name); continue
    with tempfile.TemporaryDirectory() as td:
        pdf=Path(td)/'page.pdf'; prefix=Path(td)/'page'
        r1=subprocess.run(['weasyprint',str(html),str(pdf)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        r2=subprocess.run(['pdftoppm','-png','-r','120',str(pdf),str(prefix)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        pages=sorted(Path(td).glob('page-*.png'))
        if r1.returncode or r2.returncode or not pages:
            failed.append(p.name); continue
        shutil.copy2(pages[0],outdir/'dashboard.png')
        shutil.copy2(pages[0],outdir/'dashboard_01.png')
        if len(pages)>1: shutil.copy2(pages[1],outdir/'dashboard_02.png')
        else: shutil.copy2(pages[0],outdir/'dashboard_02.png')
print('Screenshot render failures:',failed)
sys.exit(1 if failed else 0)
