from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('05', project_root)
    build_dashboard(project_root, 'Data Science Skills Mastery Lab', 'End-to-end data science skills', 'EDA, scaling, PCA, classification, cross-validation, feature importance and model evaluation using the Iris dataset.')
    print(metrics)
