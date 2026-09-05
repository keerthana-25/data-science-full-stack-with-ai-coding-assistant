from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('10', project_root)
    build_dashboard(project_root, 'CRISP-DM Masters Platform', 'Integrated CRISP-DM workflow', 'One compact workflow covering EDA, KMeans, Isolation Forest, Random Forest classification, simple association rules, approximate neighbor search and synthesis.')
    print(metrics)
