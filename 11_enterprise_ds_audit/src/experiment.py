from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('11', project_root)
    build_dashboard(project_root, 'Enterprise Data Science Audit', 'Governance and reproducibility', 'Static audit of sibling projects for required files, seed usage, train/test discipline markers and documentation completeness.')
    print(metrics)
