from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import feature_standard_scaling, feature_encoding, feature_isolation_and_split, feature_merge

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
            name="feature_isolation_and_split_node")
    ]
    
    heating_train_pipeline = pipeline_modular(
        pipe=nodes,
        inputs={"csv_energy_efficiency": "cleaned_csv_energy_efficiency"},
        namespace="heating"
    )
    
    cooling_train_pipeline = pipeline_modular(
        pipe=nodes,
        inputs={"csv_energy_efficiency": "cleaned_csv_energy_efficiency"},
        namespace="cooling"
    )
    
    both_train_pipeline = pipeline_modular(
        pipe=nodes,
        inputs={"csv_energy_efficiency": "cleaned_csv_energy_efficiency"},
        namespace="both"
    )
    
    return heating_train_pipeline + cooling_train_pipeline + both_train_pipeline