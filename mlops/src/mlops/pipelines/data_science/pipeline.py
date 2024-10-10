from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import feature_standard_scaling, feature_encoding, feature_merge

def create_pipeline(**kwargs) -> Pipeline:
    nodes_train = [
        node(
            func=feature_standard_scaling,
            inputs=["train_csv_energy_efficiency", "params:features"],
            outputs="train_scaled_csv_energy_efficiency",
            name="feature_standard_scaling_node"
        ),
        node(
            func=feature_encoding,
            inputs=["train_csv_energy_efficiency", "params:features"],
            outputs="train_encoded_csv_energy_efficiency",
            name="feature_encoding_node"
        ),
        node(
            func=feature_merge,
            inputs=["train_scaled_csv_energy_efficiency", "train_encoded_csv_energy_efficiency"],
            outputs="train_processed_csv_energy_efficiency",
            name="feature_merge_node"
        )
    ]
    
    nodes_test = [
        node(
            func=feature_standard_scaling,
            inputs=["{namespace}.train_csv_energy_efficiency", "params:root"],
            outputs="test_scaled_csv_energy_efficiency",
            name="feature_standard_scaling_node"
        ),
        node(
            func=feature_encoding,
            inputs=["{namespace}.train_csv_energy_efficiency", "params:root"],
            outputs="test_encoded_csv_energy_efficiency",
            name="feature_encoding_node"
        ),
        node(
            func=feature_merge,
            inputs=["test_scaled_csv_energy_efficiency", "test_encoded_csv_energy_efficiency"],
            outputs=["test_processed_csv_energy_efficiency"],
            name="feature_merge_node"
        )
    ]
    
    heating_train_pipeline = pipeline_modular(
        pipe=nodes_train,
        inputs={"train_csv_energy_efficiency": "heating.train_csv_energy_efficiency"},
        namespace="heating"
    )
    
    cooling_train_pipeline = pipeline_modular(
        pipe=nodes_train,
        inputs={"train_csv_energy_efficiency": "cooling.train_csv_energy_efficiency"},
        namespace="cooling"
    )
    
    return heating_train_pipeline + cooling_train_pipeline