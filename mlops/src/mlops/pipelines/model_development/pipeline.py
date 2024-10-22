from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import estimate_r2_xgb_model, estimate_mse_xgb_model


def create_pipeline(**kwargs) -> Pipeline:
    node_list = [
        node(
            func=estimate_r2_xgb_model,
            inputs=["train_energy_efficiency", "target_energy_efficiency", "params:grid", "params:namespace"],
            outputs=["selection_best_xg_r2_model", "selection_best_xg_r2_metric"],
            name="estimate_xgboost_r2_model"
        ),
        node(
            func=estimate_mse_xgb_model,
            inputs=["train_energy_efficiency", "target_energy_efficiency", "params:grid", "params:namespace"],
            outputs=["selection_best_xg_mse_model", "selection_best_xg_mse_metric"],
            name="estimate_xgboost_mse_model"
        )
    ]
    
    heating_train_pipe = pipeline_modular(
            pipe=node_list,
            inputs={
                "train_energy_efficiency": f"heating.energy_efficiency_train",
                "target_energy_efficiency": f"heating.target_energy_efficiency_train"
            },
            parameters={"params:namespace": "heating_train.name"},
            namespace="heating_train"
        )
    
    
    cooling_train_pipe = pipeline_modular(
            pipe=node_list,
            inputs={
                "train_energy_efficiency": f"cooling.energy_efficiency_train",
                "target_energy_efficiency": f"cooling.target_energy_efficiency_train"
            },
            parameters={"params:namespace": "cooling_train.name"},
            namespace="cooling_train"
        )
    
    
    return heating_train_pipe + cooling_train_pipe