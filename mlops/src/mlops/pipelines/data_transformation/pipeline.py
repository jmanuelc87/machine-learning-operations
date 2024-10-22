from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import rename_columns, remove_null_values, separate_targets, feature_standard_scaling, feature_encoding, feature_merge, features_train_test_split


def create_pipeline(**kwargs) -> Pipeline:
    base_nodes_list = [
        node(
            func=rename_columns,
            inputs=["energy_efficiency"],
            outputs="renamed_energy_efficiency",
            name="rename_columns_node"
        ),
        
        node(
            func=remove_null_values,
            inputs=["raw_energy_efficiency"],
            outputs="energy_efficiency",
            name="remove_na_node"
        )
    ]
    
    base_pipe = pipeline(base_nodes_list)
    
    separate_targets_node = node(
        func=separate_targets,
        inputs=["renamed_energy_efficiency"],
        outputs=["features_energy_efficiency", "target_heating_energy_efficiency", "target_cooling_energy_efficiency"]
    )
    
    separate_targets_pipe = pipeline([separate_targets_node])
    
    processing_nodes_list = [
        node(
            func=feature_standard_scaling,
            inputs=["features_energy_efficiency"],
            outputs=["scaled_energy_efficiency", "scaler_artifact"],
            name="feature_standard_scaling_node"
        ),
        node(
            func=feature_encoding,
            inputs=["features_energy_efficiency"],
            outputs=["encoded_energy_efficiency", "encoding_artifact"],
            name="feature_encoding_node"
        ),
        node(
            func=feature_merge,
            inputs=["scaled_energy_efficiency", "encoded_energy_efficiency"],
            outputs="merged_energy_efficiency",
            name="feature_merge_node"
        )
    ]
    
    processing_pipe = pipeline(processing_nodes_list)
    
    features_train_test_split_node = node(
        func=features_train_test_split,
        inputs=["energy_efficiency", "target_energy_efficiency", "params:features"],
        outputs=["energy_efficiency_train", "energy_efficiency_test", "target_energy_efficiency_train", "target_energy_efficiency_test"]
    )
    
    heating_split_pipe = pipeline_modular(
        pipe=[features_train_test_split_node],
        inputs={
            "energy_efficiency":"merged_energy_efficiency",
            "target_energy_efficiency": "target_heating_energy_efficiency"
        },
        namespace="heating"
    )
    
    cooling_split_pipe = pipeline_modular(
        pipe=[features_train_test_split_node],
        inputs={
            "energy_efficiency":"merged_energy_efficiency",
            "target_energy_efficiency": "target_cooling_energy_efficiency"
        },
        namespace="cooling"
    )
    
    return base_pipe + separate_targets_pipe + processing_pipe + heating_split_pipe + cooling_split_pipe