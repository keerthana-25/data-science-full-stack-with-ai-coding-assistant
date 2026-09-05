from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('12', project_root)
    build_dashboard(project_root, 'TimePulse Forecasting Engine', 'Time series forecasting', 'Chronological split, lag features, linear and random-forest forecasts, MAE/RMSE comparison, no random shuffling.')
    print(metrics)
