import logging
from zenml import step
import pandas as pd
from sklearn.linear_model import LogisticRegression
from typing import Annotated

logger = logging.getLogger(__name__)

@step
def train_model(
    X: pd.DataFrame,
    y: pd.DataFrame,
    rs: int
) -> Annotated[LogisticRegression,'logistic_model']:
    '''
    Function to train a regularized logistic regression model
    using preprocessed data
    Args:
        X: pd.DataFrame with features
        y: pd.DataFrame with labels
        rs: int of random state
    Returns:
        LogisticRegression model
    '''
    try:
        # L2 regularization penalty has the shape w_1^2 + ... + w_n^2
        # where w_i is the ith weigth the model gets. This regularization
        # helps the model to avoid overfitting, pushing weights to 0.
        penalty = 'l2'

        # C is the inverse of the regularization strength
        C = 0.1

        # generate  Linnear Regression Model
        model = LogisticRegression(penalty=penalty, C=C, random_state=rs)

        # fit model
        model.fit(X, y)

        return model
    except Exception as e:
        logger.error(f"❌ Error at training step: {e}")
        raise