import mlflow
import numpy as np
import pandas as pd

from sklearn.model_selection import GridSearchCV, cross_val_score
from xgboost import XGBRegressor


def estimate_model(X: pd.DataFrame, y: pd.DataFrame, params, metric, Model):
    _model = Model()
    
    grid_search = GridSearchCV(
        estimator=_model,
        param_grid=params['grid'],
        scoring=metric,
        cv=4,
        n_jobs=-1,
        verbose=0
    )
    
    grid_search.fit(X, y)
    
    return grid_search.best_estimator_, grid_search.best_score_, pd.DataFrame(data=[grid_search.best_params_])


def estimate_r2_xgb_model(X: pd.DataFrame, y: pd.DataFrame, params):
    SelectedModel = XGBRegressor
    return estimate_model(X, y, params, 'r2', SelectedModel)


def estimate_mse_xgb_model(X: pd.DataFrame, y: pd.DataFrame, params):
    SelectedModel = XGBRegressor
    return estimate_model(X, y, params, 'neg_mean_squared_error', SelectedModel)
