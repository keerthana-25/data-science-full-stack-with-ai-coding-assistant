from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('14', project_root)
    build_dashboard(project_root, 'Multimodal AutoML Suite', 'Multimodal classification', 'Combines tabular, simple text-count and image-summary features, then runs an automated classifier tournament. AutoGluon is optional when installed.')
    print(metrics)
