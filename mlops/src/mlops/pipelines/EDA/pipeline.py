"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""
from kedro.pipeline import Pipeline, node
from .nodes import load_data, rename_columns, get_data_shape # Importamos las funciones de el archivo .node 

# 1) Definimos los nodos de forma individual

# 1.1) Definir el nodo de lectura de datos 
reading_data = node(
            func= load_data,
            inputs="params:raw_data_filepath", # La funcion load_data requiere un parámetro, en este caso se definiio en el archivo de paraetres y es un  string donde se define la dirección del archivo 
            outputs="raw_dataset", # Nombre de su output 
            name="load_data_node") #nombre del nodo 


# 1.2) Definición del nodo de cambio de nombre 
rename =  node (
    func=rename_columns,
    inputs="raw_dataset", # vease que es el output del nodo anterior 
    outputs="renamed_dataset",
    name="rename_columns_node"
)


# Kedro se encarga de pasar el dataset al primer parámetro de la función rename_node.
# 1.3) Definir el nodo boxplot_node
boxplot = node(
    func=boxplot_node,  # Función que será llamada en este nodo
    inputs="renamed_data",  # Utiliza los datos de salida del nodo anterior
    outputs=None,  # Este nodo no produce un set de datos, simplemente visualiza
    name="boxplot_node"  # Nombre del nodo para identificarlo en el pipeline
)


# 1.4) Definir el nodo de shape 
shape = node(
            func=get_data_shape,
            inputs="renamed_dataset", # Utiliza el output del nodo anterior 
            outputs="data_shape",
            name="get_data_shape_node"
        )


# 2) Integración de nodos
def create_pipeline(**kwargs):
    return Pipeline(
        # Definimos una lista con los nodos del pipeline en orden de ejecución 
        [ reading_data, rename, boxplotshape]
    )