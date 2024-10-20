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

def _log_mlflow(metric_name, score, model_name, model_params, estimator, input):
    mlflow.log_params(model_params)
    mlflow.log_metric(metric_name, score)
    if model_name != 'xgboost':
        mlflow.sklearn.log_model(sk_model=estimator, input_example=input, artifact_path=model_name)
    else:
        mlflow.xgboost.log_model(xgb_model=estimator, input_example=input, artifact_path=model_name)


def train_and_evaluate_model(X: pd.DataFrame, y:pd.DataFrame, model, params) -> pd.DataFrame:
    SelectedModel = model_dict[model]
    selected_model = SelectedModel(**params[model])    
    scores = cross_val_score(
            estimator=selected_model,
            X=X,
            y=y.squeeze(),
            cv=5,
            scoring='r2',
            n_jobs=-1
        )

    return pd.DataFrame(data=scores, columns=[f'r2 {model} scores'])


def selection_best_params(X: pd.DataFrame, y: pd.DataFrame, params):
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("JuanManuel_Energy_Efficiency")
    
    SelectedModel = model_dict[params['best_model']]
    _model = SelectedModel()    
    grid_search = GridSearchCV(
        estimator=_model,
        param_grid=params['best_model_params'],
        scoring=params['metric'],
        cv=6,
        n_jobs=-1,
        verbose=0
    )
    
    with mlflow.start_run(tags=params['tags']):
        grid_search.fit(X, y)
        _log_mlflow(params['metric'], grid_search.best_score_, params['best_model'], grid_search.best_params_, grid_search.best_estimator_, X)
    
    return _model