from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import feature_standard_scaling, feature_encoding, feature_isolation_and_split, feature_merge, train_evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            func=feature_standard_scaling,
            inputs=["csv_energy_efficiency", "params:features"],
            outputs="scaled_csv_energy_efficiency",
            name="feature_standard_scaling_node"
        ),
        node(
            func=feature_encoding,
            inputs=["csv_energy_efficiency", "params:features"],
            outputs="encoded_csv_energy_efficiency",
            name="feature_encoding_node"
        ),
        node(
            func=feature_merge,
            inputs=["scaled_csv_energy_efficiency", "encoded_csv_energy_efficiency"],
            outputs="processed_csv_energy_efficiency",
            name="feature_merge_node"
        ),
        node(
            func=feature_isolation_and_split,
            inputs=["processed_csv_energy_efficiency", "csv_energy_efficiency", "params:features"],
            outputs=["train_csv_energy_efficiency", "test_csv_energy_efficiency", "train_target_csv_energy_efficiency", "test_target_csv_energy_efficiency"],
            name="feature_isolation_and_split_node"),
    ]
    
    
    train_evaluate_model_nodes = [
        node(
            func=train_evaluate_model,
            inputs=["train_csv_energy_efficiency", "train_target_csv_energy_efficiency", "params:features"],
            outputs="model_results",
            name="train_evaluate_model_node"
        )
    ]
    
    heating_train_pipeline = pipeline_modular(
        pipe=nodes + train_evaluate_model_nodes,
        inputs={"csv_energy_efficiency": "cleaned_csv_energy_efficiency"},
        namespace="heating"
    )
    
    cooling_train_pipeline = pipeline_modular(
        pipe=nodes + train_evaluate_model_nodes,
        inputs={"csv_energy_efficiency": "cleaned_csv_energy_efficiency"},
        namespace="cooling"
    )
    
    return heating_train_pipeline + cooling_train_pipeline