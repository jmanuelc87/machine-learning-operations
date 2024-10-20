"""
This is a boilerplate pipeline 'data_transformation'
generated using Kedro 0.19.9
"""

from kedro.pipeline import Pipeline, pipeline
from kedro.pipeline import Pipeline, node
from .nodes import *  # Importamos todas las funciones del script de nodes 

################                       DECLARACION DE NODOS                  ###############

# 1.1) Nodo de lectura de datos 
reading_data = node(
    func=load_data,
    inputs="params:raw_data_filepath",  # Prefix with 'params:', el match ocurre por posicion. Podria ponder una lista de parametros y  se colocarian en el mismo orden a la función que estoy utilizando. 
    outputs="raw_dataset",
    name="load_data_node")

# 1.2) Nodo rename 
rename = node(
    func=rename_columns,
    inputs="raw_dataset",
    outputs="renamed_dataset",
    name="rename_columns_node")


# 1.3) Declaración del nodo de datasplit 
data_split_node = node(
    func=data_split,
    inputs="renamed_dataset", # set de datos de entrada, recordemos que este set de datos se crea a partir de otro Pipeline 
    outputs=["X_train", 
             "X_test", 
             "cooling_train", 
             "cooling_test", 
             "heating_train", 
             "heating_test"],  # Multiple outputs como una lista 
    name="data_split_node")


# 1.4) Nodo de escalamiento, se aplica a mi set de datos de entrenamiento 
scaling = node(
    func=scaling,
    inputs="X_train",
    outputs="Scaled_X_train",
    name="Scaling")




#################                     2) INTEGRACION DE NODOS          ###################
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            reading_data, 
            rename, 
            data_split_node, 
            scaling

        ]
    )