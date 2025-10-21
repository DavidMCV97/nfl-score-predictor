import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Reads data from a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.
    Returns:
        pd.DataFrame: The data read from the CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        logger.info(f'Data ingested successfully from {file_path}. Shape: {data.shape}')
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logger.error(f"Empty CSV file: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading data from {file_path}: {str(e)}")
        raise