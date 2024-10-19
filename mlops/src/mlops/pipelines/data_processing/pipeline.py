from kedro.pipeline import Pipeline, pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular
from .nodes import rename_columns, remove_null_values


def create_pipeline(**kwargs) -> Pipeline:
    base_nodes = [
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
    
    return pipeline_modular(
        pipe=base_nodes,
        inputs="raw_energy_efficiency",
        namespace="data_processing"
    )