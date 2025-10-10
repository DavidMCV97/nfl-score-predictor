import sys
from pathlib import Path

# make sure the project root is in sys.path
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.append(project_root)

from src.data_ingestion.data_ingestion import load_csv
from src.logger import setup_logging

setup_logging()

df = load_csv("datasets/games.csv")