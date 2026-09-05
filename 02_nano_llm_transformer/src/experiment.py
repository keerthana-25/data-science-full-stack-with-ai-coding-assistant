from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from shared.experiments import run_project
from shared.dashboard import build_dashboard

if __name__ == '__main__':
    project_root=Path(__file__).resolve().parents[1]
    metrics=run_project('02', project_root)
    build_dashboard(project_root, 'NanoLlama Language Model Lab', 'Language modeling', 'Small character n-gram language-model baseline with deterministic training corpus, perplexity estimate, and text generation. Kept intentionally laptop-friendly.')
    print(metrics)
