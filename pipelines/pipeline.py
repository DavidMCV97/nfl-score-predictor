from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.validate_data import validate_data
from src.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

@pipeline
def test_pipeline(data_path:str, config_path:str):
    '''
    zenml pipeline for tests during programation
    Args:
        data_path: str to data file
        config_path: str to config.yaml file
    '''
    df = ingest_data(data_path)
    valid = validate_data(df, config_path)