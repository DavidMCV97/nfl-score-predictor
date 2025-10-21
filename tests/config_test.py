import sys
from pathlib import Path

# make sure the project root is in sys.path
project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.append(project_root)

import yaml

config_path = 'config/config.yaml'

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

print(config)