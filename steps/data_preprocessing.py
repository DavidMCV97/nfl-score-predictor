import logging
from zenml import step
import pandas as pd

logger = logging.getLogger(__name__)

@step
def data_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    '''
    function to clean and transform raw data.
    Args:
        df: pd.DataFrame with raw data
    Returns:
        pd.DataFrame (cleaned and transformed data)
    '''

    