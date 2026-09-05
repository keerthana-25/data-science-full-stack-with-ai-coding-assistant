from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('04', project_root)
    build_dashboard(project_root, 'Market Basket Pattern Mining', 'Association rule mining', 'Deterministic basket transactions, item and pair support, confidence and lift calculation, top association rules.')
    print(metrics)
