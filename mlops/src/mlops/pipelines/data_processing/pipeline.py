from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular
from .nodes import convert_to_csv, rename_columns, feature_isolation_and_split, remove_null_values


def create_pipeline(**kwargs) -> Pipeline:
    base_pipeline = pipeline([
        node(
            func=convert_to_csv,
            inputs=["raw_energy_efficiency"],
            outputs="csv_energy_efficiency",
            name="convert_to_csv_node"
        ),
        
        node(
            func=rename_columns,
            inputs=["csv_energy_efficiency", "params:rename_columns"],
            outputs="csv_renamed_energy_efficiency",
            name="rename_columns_node"
        ),
        
        node(
            func=remove_null_values,
            inputs=["csv_energy_efficiency"],
            outputs="cleaned_csv_energy_efficiency",
            name="remove_na_node"
        )
    ])
    
    feature_isolation_and_split_node = node(
                        func=feature_isolation_and_split,
                        inputs=["cleaned_csv_energy_efficiency", "params:root"],
                        outputs=["train_csv_energy_efficiency", "test_csv_energy_efficiency", "train_target_csv_energy_efficiency", "test_target_csv_energy_efficiency"],
                        name="feature_isolation_and_split_node")
    
    heating_pipeline = pipeline_modular(
        pipe=[feature_isolation_and_split_node],
        inputs=["cleaned_csv_energy_efficiency"],
        namespace="heating"
    )
    
    cooling_pipeline = pipeline_modular(
        pipe=[feature_isolation_and_split_node],
        inputs=["cleaned_csv_energy_efficiency"],
        namespace="cooling"
    )
    
    return base_pipeline + heating_pipeline + cooling_pipeline