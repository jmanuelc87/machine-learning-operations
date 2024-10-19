"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""
from kedro.pipeline import Pipeline, node
from .nodes import  * # importamos las funciones  


#######################             DEFINICION DEL PIPELINE DE EJUCION DE EDA           ###################

# 1) Define individual nodes

# MUY IMPORTANTE: a cada nodo, en la funcion de input le puedes indicar parametros o datos, si le vas a meter parametros que pasaran a la funcion tienen que usar el prefijo params: 
# 1.1) Data reading node
reading_data = node(
    func=load_data,
    inputs="params:raw_data_filepath",  # Prefix with 'params:', el match ocurre por posicion. Podria ponder una lista de parametros y  se colocarian en el mismo orden a la función que estoy utilizando 
    outputs="raw_dataset",
    name="load_data_node")

# 1.2) Rename node
rename = node(
    func=rename_columns,
    inputs="raw_dataset",
    outputs="renamed_dataset",
    name="rename_columns_node")


# 1.3) Shape node
shape = node(
    func=get_data_shape,
    inputs="renamed_dataset",
    outputs="data_shape",
    name="get_data_shape_node")


# 1.4) Nodo de estadistica descriptiva 
description = node(
    func=descriptive_statistics,
    inputs="renamed_dataset",
    outputs="descriptive_statistics_excel",  # Reference the catalog output
    name="descriptive_statistics")


# 1.5) Nodo de histogramas 
histograms  = node(
    func=histograms,
    inputs= "renamed_dataset", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "histograms",  # Reference the catalog output
    name= "Histograms")

# 1.6) Nodo de histogramas 
boxplots = node(
    func= boxplots,
    inputs= "renamed_dataset", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "boxplots",  # Reference the catalog output
    name= "boxplots")

# 1.7) Heatmap 
heatmap = node(
    func= heatmap,
    inputs= "renamed_dataset", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "heatmap",  # Reference the catalog output
    name= "heatmap")



# 2) Integrate nodes
def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            reading_data,
            rename,
            shape,
            description , 
            histograms, 
            boxplots, 
            heatmap 
        ]
    )