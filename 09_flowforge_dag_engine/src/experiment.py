from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('09', project_root)
    build_dashboard(project_root, 'FlowForge DAG Engine', 'Data pipeline orchestration', 'Directed acyclic graph validation, topological execution order, task status simulation and dependency visualization.')
    print(metrics)
