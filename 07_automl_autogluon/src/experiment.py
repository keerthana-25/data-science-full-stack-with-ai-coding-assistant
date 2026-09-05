from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('07', project_root)
    build_dashboard(project_root, 'AutoML Model Tournament', 'Automated model selection', 'Lightweight AutoML-style tournament across logistic regression, random forest, gradient boosting and KNN using cross-validation. README includes optional AutoGluon upgrade path.')
    print(metrics)
