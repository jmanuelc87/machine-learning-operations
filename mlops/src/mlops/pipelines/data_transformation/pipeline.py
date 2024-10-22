from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import rename_columns, remove_null_values, separate_targets, feature_standard_scaling, feature_encoding, feature_merge, features_train_test_split


def create_pipeline(**kwargs) -> Pipeline:
    base_nodes_list = [
        node(
            func=rename_columns,
            inputs=["csv_energy_efficiency", "params:rename_columns"],
            outputs="csv_renamed_energy_efficiency",
            name="rename_columns_node"
        ),
        
        node(
            func=remove_null_values,
            inputs=["raw_energy_efficiency"],
            outputs="csv_energy_efficiency",
            name="remove_na_node"
        )
    ]
    
    base_pipe = pipeline(base_nodes_list)
    
    separate_targets_node = node(
        func=separate_targets,
        inputs=["csv_renamed_energy_efficiency"],
        outputs=["csv_features_energy_efficiency", "csv_target_heating_energy_efficiency", "csv_target_cooling_energy_efficiency"]
    )
    
    separate_targets_pipe = pipeline([separate_targets_node])
    
    processing_nodes_list = [
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
        pipe=processing_nodes_list,
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
    
    return base_pipe + separate_targets_pipe + processing_pipe + heating_split_pipe + cooling_split_pipe