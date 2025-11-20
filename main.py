from pipelines.pipeline import test_pipeline
from src.logger import setup_logging

data_path = 'datasets/games.csv'
config_path = 'config/config.yaml'
max_year = 2024
cutoff_year = 2023

def main(data_path: str, config_path: str, max_year: int, cutoff_year: int):
    setup_logging()
    test_pipeline(data_path, config_path, max_year, cutoff_year)

if __name__ == '__main__':
    main(data_path, config_path, max_year, cutoff_year)