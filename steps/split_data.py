import logging
from zenml import step
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple

logger = logging.getLogger(__name__)

@step
def split_data(
    df: pd.DataFrame, 
    test_size: float = 0.2, 
    random_state: int = None
) -> Tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    '''
    Splitting data into train and test sets
    Args:
        df: input dataframe
        test_size: proportion of the dataset to include in the test split
        random_state: controls the shuffling applied to the data before applying the split
    Returns:
        pd.Dataframe (train_df)
        pd.Dataframe (test df)
    '''
    try:
        # notification of step start
        logger.info("Starting data splitting...")

        # drop unnecessary columns + target
        X = df[['focus_team_status','game_type','focus_team_ltg_wins','focus_team_ltg_score','day_period']]

        # target variable
        y = df['winner']

        # perform the split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # return the splits
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        logger.error(f"❌ Data splitting step failed: {str(e)}")
        raise