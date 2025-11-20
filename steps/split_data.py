import logging
from zenml import step
import pandas as pd
from typing import Tuple, Annotated

logger = logging.getLogger(__name__)

@step
def split_data(
    df: pd.DataFrame, 
    cutoff_year: int
) -> Tuple[
    Annotated[pd.DataFrame, 'X_train'],
    Annotated[pd.DataFrame, 'X_test'],
    Annotated[pd.Series, 'y_train'],
    Annotated[pd.Series, 'y_test']
]:
    '''
    Splitting data into train and test sets
    Args:
        df: input dataframe
        cutoff_year: int, first year to consider for test set
    Returns:
        pd.Dataframe (train_df)
        pd.Dataframe (test df)
    '''
    try:
        # season info
        season = df['season']

        # drop unnecessary columns + target
        X = df[['focus_team_status','game_type',
                'focus_team_ltg_wins','focus_team_ltg_score',
                'versus_team_ltg_wins','versus_team_ltg_score',
                'day_period']]

        # target variable
        y = df['winner']

        # perform the split
        X_train = X[season < cutoff_year]
        y_train = y[season < cutoff_year]
        X_test = X[season >= cutoff_year]
        y_test = y[season >= cutoff_year]

        # return the splits
        return X_train, X_test, y_train, y_test
    
    except Exception as e:
        logger.error(f"❌ Data splitting step failed: {str(e)}")
        raise