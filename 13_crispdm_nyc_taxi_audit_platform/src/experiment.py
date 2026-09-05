from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('13', project_root)
    build_dashboard(project_root, 'CRISP-DM NYC TLC Audit Platform', 'Audited regression and explainability', 'NYC-like regression with chronological-style partitioning, model comparison, feature importance, clustering of pickup coordinates and explicit audit checks.')
    print(metrics)
