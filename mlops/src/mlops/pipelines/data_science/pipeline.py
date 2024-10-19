from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import feature_standard_scaling, feature_encoding, feature_merge, separate_targets, features_train_test_split


def create_pipeline(**kwargs) -> Pipeline:
    separate_targets_node = node(
        func=separate_targets,
        inputs=["csv_separate_energy_efficiency"],
        outputs=["csv_features_energy_efficiency", "csv_target_heating_energy_efficiency", "csv_target_cooling_energy_efficiency"]
    )
    
    separate_targets_pipe = pipeline(
        [separate_targets_node]
    )
    
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
            outputs="merged_csv_energy_efficiency",
            name="feature_merge_node"
        )
    ]
    
    processing_pipe = pipeline_modular(
        pipe=nodes,
        inputs={
            "csv_energy_efficiency": "csv_features_energy_efficiency"
        },
        namespace="processing"
    )
    
    features_train_test_split_node = node(
            func=features_train_test_split,
            inputs=["csv_energy_efficiency", "csv_target_energy_efficiency", "params:features"],
            outputs=["csv_energy_efficiency_train", "csv_energy_efficiency_test", "csv_target_energy_efficiency_train", "csv_target_energy_efficiency_test"]
        )
    
    heating_split_pipe = pipeline_modular(
        pipe=[features_train_test_split_node],
        inputs={
            "csv_energy_efficiency":"processing.merged_csv_energy_efficiency",
            "csv_target_energy_efficiency": "csv_target_heating_energy_efficiency"
        },
        namespace="heating"
    )
    
    cooling_split_pipe = pipeline_modular(
        pipe=[features_train_test_split_node],
        inputs={
            "csv_energy_efficiency":"processing.merged_csv_energy_efficiency",
            "csv_target_energy_efficiency": "csv_target_cooling_energy_efficiency"
        },
        namespace="cooling"
    )
    
    data_science_pipe = pipeline_modular(
        pipe=[separate_targets_pipe + processing_pipe + heating_split_pipe + cooling_split_pipe],
        inputs={
            "csv_separate_energy_efficiency": "data_processing.csv_energy_efficiency"
        },
        namespace="data_science")
    
    return data_science_pipe