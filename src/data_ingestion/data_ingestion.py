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
        logger.info('data ingested', extra={'path':file_path})
        return data
    except Exception as e:
        print(f"Error reading the data from {file_path}: {e}")
        raise