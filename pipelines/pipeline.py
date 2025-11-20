from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.validate_data import validate_data
from steps.data_preprocessing import data_preprocessing, post_split_preprocessing
from steps.split_data import split_data
import logging

logger = logging.getLogger(__name__)

@pipeline
def test_pipeline(data_path:str, config_path:str, max_year:int, cutoff_year:int):
    '''
    zenml pipeline for tests during programation.
    Args:
        data_path: str to data file
        config_path: str to config.yaml file
    '''
    df = ingest_data(data_path)
    valid, validated_df = validate_data(df, config_path)
    if valid:
        processed_df = data_preprocessing(validated_df, max_year, config_path=config_path)
        X_train, X_test, y_train, y_test = split_data(processed_df, cutoff_year)
        X_train_processed, y_train_processed = post_split_preprocessing(X_train, y_train)
    else:
        logger.error("Data validation failed. Pipeline terminated.")