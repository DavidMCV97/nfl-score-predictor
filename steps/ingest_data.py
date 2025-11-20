from src.data_ingestion.data_ingestion import load_csv
from zenml import step
import pandas as pd
import logging
from typing import Annotated

logger = logging.getLogger(__name__)

@step
def ingest_data(data_path:str) -> Annotated[pd.DataFrame, 'raw_games_data']:
    '''
    Ingesting data from data_path
    Args:
        data_path: path to the data
    Returns:
        pd.DataFrame: the ingested data
    '''
    try:
        df = load_csv(data_path)
        return df
    except Exception as e:
        logger.error(f"❌ Data ingestion step failed: {str(e)}")
        raise