import logging
from zenml import step
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from typing import Annotated

logger = logging.getLogger(__name__)

@step
def evaluate_model(
    model: LogisticRegression,
    X: pd.DataFrame,
    y: pd.DataFrame,
    status_encoder: LabelEncoder,
    period_encoder: OneHotEncoder,
    scaler: StandardScaler
):
    '''
    function to implement evaluation step on logistic regression
    Args:
        model: LogisticRegression model
        X: pd.DataFrame of test features
        y: pd.DataFrame of test labels
    '''
    try:
        # first we addecuate test data to model
        # we repeat the steps from post split preprocessing
        X_proc = X.copy()
        y_proc = y.copy()
        X_proc['focus_team_status_encoded'] = status_encoder.transform(X_proc['focus_team_status'])
        X_proc = X_proc.drop(columns=['focus_team_status'])
        mapping = {'REG':1, 'WC':2, 'DIV':3, 'CON':4, 'SB':5}
        X_proc['game_type_encoded'] = X_proc['game_type'].map(mapping)
        X_proc = X_proc.drop(columns=['game_type'])
        day_period_encoded = period_encoder.transform(X_proc[['day_period']])
        day_period_df = pd.DataFrame(
            day_period_encoded,
            columns = period_encoder.get_feature_names_out(['day_period']),
            index = X_proc.index
        )
        X_proc = X_proc.join(day_period_df)
        X_proc = X_proc.drop(columns=['day_period'])
        cols = ['focus_team_ltg_wins','focus_team_ltg_score','versus_team_ltg_wins','versus_team_ltg_score']
        new_cols = ['focus_team_ltg_wins_scaled','focus_team_ltg_score_scaled',
                    'versus_team_ltg_wins_scaled','versus_team_ltg_score_scaled']
        X_proc[new_cols] = scaler.transform(X_proc[cols])
        X_proc = X_proc.drop(columns=cols)

        # finally we evalute
        accuracy = model.score(X_proc, y_proc)

        logger.info(f'MODEL ACCURACY = {accuracy:.2f}')
    
    except Exception as e:
        logger.error(f"❌ Unexpected error at evaluation step: {e}")
        raise