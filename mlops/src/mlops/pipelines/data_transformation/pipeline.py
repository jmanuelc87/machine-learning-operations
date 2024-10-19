"""
This is a boilerplate pipeline 'data_transformation'
generated using Kedro 0.19.9
"""

from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import Pipeline, node
from .nodes import *  # Importamos todas las funciones del script de nodes 

# 1) Declaración del nodo de datasplit 
data_split_node = node(
    func=data_split,
    inputs="renamed_dataset", # set de datos de entrada, recordemos que este set de datos se crea a partir de otro Pipeline 
    outputs=("X_train", "X_test", 
             "cooling_train", "cooling_test", 
             "heating_train", "heating_test"),  # Multiple outputs as a tuple
    name="data_split_node"
)


# 2) Integrate nodes
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            data_split_node
        ]
    )