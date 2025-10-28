from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.validate_data import validate_data
from steps.data_preprocessing import data_preprocessing
from src.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

@pipeline
def test_pipeline(data_path:str, config_path:str, max_year:int):
    '''
    zenml pipeline for tests during programation
    Args:
        data_path: str to data file
        config_path: str to config.yaml file
    '''
    df = ingest_data(data_path)
    valid, validated_df = validate_data(df, config_path)
    if valid:
        processed_df = data_preprocessing(validated_df, max_year=2024, config_path=config_path)
    else:
        logger.error("Data validation failed. Pipeline terminated.")