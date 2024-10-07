"""
This is a boilerplate pipeline 'ML'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node
from .nodes import boxplot_node, rename_node


# 1) Definimos los nodos de forma individual

# 1.1) Definir el nodo rename_node
rename = node(
    func=rename_node,  # Función que será llamada en este nodo
    inputs="raw_data",  # Set de datos de entrada, tal como se indica en el catálogo
    outputs="renamed_data",  # Set de datos de salida, también definido en el catálogo
    name="rename_node"  # Nombre del nodo para identificarlo en el pipeline
)

# Kedro se encarga de pasar el dataset al primer parámetro de la función rename_node.

# 1.2) Definir el nodo boxplot_node
boxplot = node(
    func=boxplot_node,  # Función que será llamada en este nodo
    inputs="renamed_data",  # Utiliza los datos de salida del nodo anterior
    outputs=None,  # Este nodo no produce un set de datos, simplemente visualiza
    name="boxplot_node"  # Nombre del nodo para identificarlo en el pipeline
)


# 2) Integración de nodos
def create_pipeline(**kwargs):
    return Pipeline(
        [
            rename,  # Integramos el nodo rename_node
            boxplot  # Integramos el nodo boxplot_node
        ]
    )

