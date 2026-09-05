from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('15', project_root)
    build_dashboard(project_root, 'SPY Time Series Forecasting Lab', 'Financial time series', 'Leakage-safe lagged-return forecasting with walk-forward holdout, directional accuracy, RMSE and simple long/cash strategy diagnostics. Real SPY CSV can replace offline synthetic data.')
    print(metrics)
