import mlflow
import pandas as pd

from sklearn.model_selection import cross_val_score, GridSearchCV
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
    mlflow.set_experiment("Energy_Efficiency")
    
    SelectedModel = model_dict[params['best_model']]
    
    _model = SelectedModel()
    grid_search = GridSearchCV(
        estimator=_model,
        param_grid=params['best_model_params'],
        cv=6,
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X=X, y=y)

    with mlflow.start_run():

        mlflow.log_params(grid_search.best_params_)
        mlflow.log_metric("r2", grid_search.best_score_)

        if params['best_model'] != 'xgboost':
            mlflow.sklearn.log_model(sk_model=grid_search.best_estimator_, input_example=X, artifact_path=params['best_model'])
        else:
            mlflow.xgboost.log_model(xgb_model=grid_search.best_estimator_, input_example=X, artifact_path=params['best_model'])

    return grid_search.best_estimator_