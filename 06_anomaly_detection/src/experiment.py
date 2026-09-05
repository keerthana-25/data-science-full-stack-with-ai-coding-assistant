from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('06', project_root)
    build_dashboard(project_root, 'Anomaly Threat Intelligence', 'Anomaly detection', 'Synthetic normal and anomalous points, Isolation Forest scoring, ROC-AUC evaluation, visual inspection.')
    print(metrics)
