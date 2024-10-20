import mlflow
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


mlflow.set_tracking_uri("http://127.0.0.1:5000")

experiment = mlflow.set_experiment("Energy_Efficiency")

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

    # with mlflow.start_run():
        
    #     mlflow.log_params(params[model])
    #     mlflow.log_metric("r2", scores.mean())
        
    #     if model != 'xgboost':
    #         mlflow.sklearn.log_model(sk_model=selected_model, input_example=X, artifact_path=model)
    #     else:
    #         mlflow.xgboost.log_model(xgb_model=selected_model, input_example=X, artifact_path=model)

    return pd.DataFrame(data=scores, columns=[f'r2 {model} scores'])