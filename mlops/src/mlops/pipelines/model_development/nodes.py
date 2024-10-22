import mlflow
import numpy as np
import pandas as pd

from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


model_dict = {
    "linear-regression": LinearRegression,
    "random-forest": RandomForestRegressor,
    "xgboost": XGBRegressor
}

def estimate_model(X: pd.DataFrame, y: pd.DataFrame, params, Model):
    _model = Model()
    
    grid_search = GridSearchCV(
        estimator=_model,
        param_grid=params['best_model_params'],
        scoring=params['metric'],
        cv=4,
        n_jobs=-1,
        verbose=0
    )
    
    grid_search.fit(X, y)
    
    return _model


def estimate_xgb_model(X: pd.DataFrame, y: pd.DataFrame, params):
    SelectedModel = XGBRegressor
    return estimate_model(X, y, params, SelectedModel)