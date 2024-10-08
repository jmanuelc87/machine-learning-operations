"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import convert_to_csv


def create_pipeline(**kwargs) -> Pipeline:
    to_csv_node = node(
        func=convert_to_csv,
        inputs=["raw_energy_efficiency"],
        outputs="csv_energy_efficiency",
        name="convert_to_csv_node"
    )
    
    
    return pipeline(
        pipe=[to_csv_node]
    )
