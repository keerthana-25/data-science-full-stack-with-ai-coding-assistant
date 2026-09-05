from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('08', project_root)
    build_dashboard(project_root, 'Data Science Visual Foundations', 'Data science education', 'Naive Bayes classifier, confusion matrix metrics, gradient descent simulation, visual learning artifacts and quiz bank.')
    print(metrics)
