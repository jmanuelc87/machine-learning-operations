from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import estimate_r2_xgb_model, estimate_mse_xgb_model, test_xgb_model


def create_pipeline(**kwargs) -> Pipeline:
    node_list = [
        node(
            func=estimate_r2_xgb_model,
            inputs=["train_energy_efficiency", "target_energy_efficiency", "params:grid", "params:namespace"],
            outputs=["selection_best_xg_r2_model", "selection_best_xg_r2_metric"],
            name="estimate_xgboost_r2_model_node"
        ),
        
        node(
            func=estimate_mse_xgb_model,
            inputs=["train_energy_efficiency", "target_energy_efficiency", "params:grid", "params:namespace"],
            outputs=["selection_best_xg_mse_model", "selection_best_xg_mse_metric"],
            name="estimate_xgboost_mse_model_node"
        ),
        
        node(
            func=test_xgb_model,
            inputs=["test_energy_efficiency", "test_target_energy_efficiency", "selection_best_xg_r2_model", "encoding_artifact", "scaler_artifact"],
            outputs=["test_rmse", "test_r2"],
            name="test_xgb_model_node"
        )
    ]
    
    heating_train_pipe = pipeline_modular(
            pipe=node_list,
            inputs={
                "train_energy_efficiency": "heating.merged_energy_efficiency",
                "target_energy_efficiency": "heating.target_energy_efficiency_train",
                "test_energy_efficiency": "heating.energy_efficiency_test",
                "test_target_energy_efficiency": "heating.target_energy_efficiency_test",
                "scaler_artifact": "heating.scaler_artifact",
                "encoding_artifact": "heating.encoder_artifact"
            },
            parameters={"params:namespace": "heating_model.name"},
            namespace="heating_model"
        )
    
    
    cooling_train_pipe = pipeline_modular(
            pipe=node_list,
            inputs={
                "train_energy_efficiency": "cooling.merged_energy_efficiency",
                "target_energy_efficiency": "cooling.target_energy_efficiency_train",
                "test_energy_efficiency": "cooling.energy_efficiency_test",
                "test_target_energy_efficiency": "cooling.target_energy_efficiency_test",
                "scaler_artifact": "cooling.scaler_artifact",
                "encoding_artifact": "cooling.encoder_artifact"
            },
            parameters={"params:namespace": "cooling_model.name"},
            namespace="cooling_model"
        )
    
    
    return heating_train_pipe + cooling_train_pipe