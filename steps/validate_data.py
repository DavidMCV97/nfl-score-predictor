import logging
from zenml import step
import pandas as pd
from typing import Tuple
import yaml

logger = logging.getLogger(__name__)




@step
def validate_data(df:pd.DataFrame, config_path:str) -> Tuple[pd.DataFrame, bool]:
    '''
    Validation of data with config values.
    Args:
        df: pd.DataFrame with the ingested data
        config_path: path to the config file
    Returns:
        Tuple[DataFrame, bool]: (validated df, is_valid)
    '''
    try:
        # get config
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        validation_config = config['data_validation']

        # 1. required columns
        missing_cols = set(validation_config['required_columns']) - set(df.columns)
        if missing_cols:
            logger.error(f'columns missing: {missing_cols}')
            is_valid = False
        else:
            logger.info(f'all columns find :)')
            is_valid = True
        return df, is_valid

    except FileNotFoundError as e:
        logger.error(f"❌ Can't find config.yaml file: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error at validation step: {e}")
        raise