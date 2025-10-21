from pipelines.pipeline import test_pipeline

data_path = 'datasets/games.csv'
config_path = 'config/config.yaml'

if __name__ == '__main__':
    test_pipeline(data_path, config_path)