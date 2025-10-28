import logging
from zenml import step
import pandas as pd
from typing import Tuple
import yaml

logger = logging.getLogger(__name__)




@step
def validate_data(df:pd.DataFrame, config_path:str) -> Tuple[bool, pd.DataFrame]:
    '''
    Function to validate raw data with config values.
    Args:
        df: pd.DataFrame with the ingested data
        config_path: path to the config file
    Returns:
        bool (is_valid)
        pd.DataFrame (the same input df)
    '''
    try:
        # get config
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # select section of config
        validation_config = config['data_validation']
        
        # errors lits 
        errors = []

        # 1. required columns
        missing_cols = set(validation_config['required_columns']) - set(df.columns)
        if missing_cols:
            errors.append(f"Missing columns: {missing_cols}")
        else:
            logger.info('All required columns found')
        
        # 2. missing values
        null_values = df[validation_config['required_columns']].isnull().sum() / len(df)
        high_nulls = null_values[null_values > validation_config['max_null_percentage']]
        if high_nulls.any():
            errors.append(f"Columns with too many nulls: {missing_cols}")
        else:
            logger.info('Null test passed')
        
        # 3. numeric limits
        for col, ranges in validation_config['numeric_ranges'].items():
            if col in df.columns:
                if df[col].min() < ranges['min'] or df[col].max() > ranges['max']:
                    errors.append(f"{col} values out of range [{ranges['min']}, {ranges['max']}]")
            else:
                errors.append(f'numerical column {col} does not exist')

        # 4. accepted categories
        for col, categories in validation_config['categorical_values'].items():
            if col in df.columns:
                invalid = set(df[col].unique()) - set(categories)
                if invalid:
                    errors.append('{invalid} categories dont exist for {col}')
            else:
                errors.append(f'categorical column {col} does not exist')
        
        # check if passed all tests
        is_valid = len(errors)==0

        return is_valid, df
    
    except FileNotFoundError as e:
        logger.error(f"❌ Can't find config.yaml file: {e}")
        raise
    except KeyError as e:
        logger.error(f"❌ key missing in config.yaml: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error at validation step: {e}")
        raise