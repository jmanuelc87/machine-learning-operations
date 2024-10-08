"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import convert_to_csv, rename_columns, calculate_correlations


def create_pipeline(**kwargs) -> Pipeline:
    to_csv_node = node(
        func=convert_to_csv,
        inputs=["raw_energy_efficiency"],
        outputs="csv_energy_efficiency",
        name="convert_to_csv_node"
    )
    
    rename_cols_node = node(
        func=rename_columns,
        inputs=["csv_energy_efficiency"],
        outputs="csv_renamed_energy_efficiency",
        name="rename_columns_node"
    )
    
    calc_correlations_node = node(
        func=calculate_correlations,
        inputs=["csv_renamed_energy_efficiency"],
        outputs="correlations_energy_efficiency",
        name="calculate_correlations_node"
    )
    
    return pipeline(
        pipe=[to_csv_node, rename_cols_node, calc_correlations_node]
    )
