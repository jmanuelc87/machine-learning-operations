import mlflow
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_percentage_error
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor


def estimate_model(X: pd.DataFrame, y: pd.DataFrame, params, metric, namespace, Model):
    _model = Model()
    
    grid_search = GridSearchCV(
        estimator=_model,
        param_grid=params,
        scoring=metric,
        cv=4,
        n_jobs=-1,
        verbose=0
    )
    
    grid_search.fit(X, y)
        
    for key in grid_search.best_params_.keys():
        mlflow.log_param(f"{namespace}.{metric}.best_param.{key}", grid_search.best_params_[key])
    
    return grid_search.best_estimator_, grid_search.best_score_
    

def estimate_r2_model(X: pd.DataFrame, y: pd.DataFrame, params, namespace):
    SelectedModel = XGBRegressor
    return estimate_model(X, y, params, 'r2', namespace, SelectedModel)


def estimate_mape_model(X: pd.DataFrame, y: pd.DataFrame, params, namespace):
    SelectedModel = XGBRegressor
    return estimate_model(X, y, params, 'neg_mean_absolute_percentage_error', namespace, SelectedModel)


def test_xgb_model(X: pd.DataFrame, y: pd.DataFrame, _model, encoder, scaler):
    X_numeric = X[["Relative Compactness", "Surface Area", "Wall Area", "Roof Area"]]
    X_categoric = X[["Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"]]
    
    categorical = encoder.transform(X_categoric)
    numeric = scaler.transform(X_numeric)
    
    categorical_df = pd.DataFrame(categorical, columns=encoder.get_feature_names_out())
    numeric_df = pd.DataFrame(numeric, columns=scaler.get_feature_names_out())
    
    categorical_df.reset_index(drop=True, inplace=True)
    numeric_df.reset_index(drop=True, inplace=True)
    
    X_test = pd.concat(objs=[numeric_df, categorical_df], axis=1)
        
    y_pred = _model.predict(X_test)
    
    rmse = mean_absolute_percentage_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    
    return rmse, r2