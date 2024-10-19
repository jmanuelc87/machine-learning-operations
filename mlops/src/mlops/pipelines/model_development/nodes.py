import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


model_dict = {
    "linear-regression": LinearRegression,
    "random-forest": RandomForestRegressor,
    "xgboost": XGBRegressor
}


def train_and_evaluate_model(X: pd.DataFrame, y:pd.DataFrame, model, params) -> pd.DataFrame:
    SelectedModel = model_dict[model]
    model = SelectedModel(**params[f'{model}'])
    scores = cross_val_score(
        estimator=model,
        X=X,
        y=y,
        scoring='r2',
        n_jobs=-1
    )
    return pd.DataFrame(data=scores, columns=[f'r2 {model} scores'])