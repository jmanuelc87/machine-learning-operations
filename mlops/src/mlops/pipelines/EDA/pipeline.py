"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline as pipeline_modular

from .nodes import  * # importamos las funciones  


#######################             DEFINICION DEL PIPELINE DE EJUCION DE EDA           ###################

# 1) Define individual nodes

# MUY IMPORTANTE: a cada nodo, en la funcion de input le puedes indicar parametros o datos, si le vas a meter parametros que pasaran a la funcion tienen que usar el prefijo params: 

# 1.4) Nodo de estadistica descriptiva 
description = node(
    func=descriptive_statistics,
    inputs="renamed_energy_efficiency",
    outputs="descriptive_statistics_excel",  # Reference the catalog output
    name="descriptive_statistics")


# 1.5) Nodo de histogramas 
histograms  = node(
    func=histograms,
    inputs= "renamed_energy_efficiency", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "histograms",  # Reference the catalog output
    name= "Histograms")

# 1.6) Nodo de histogramas 
boxplots = node(
    func= boxplots,
    inputs= "renamed_energy_efficiency", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "boxplots",  # Reference the catalog output
    name= "boxplots")

# 1.7) Heatmap 
heatmap = node(
    func= heatmap,
    inputs= "renamed_energy_efficiency", # Toma un set de datos como input, declarado en el catalogo 
    outputs= "heatmap",  # Reference the catalog output
    name= "heatmap")



# 2) Integrate nodes
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline_modular(
        [
            description, 
            histograms, 
            boxplots, 
            heatmap
        ],
        inputs={"renamed_energy_efficiency": "renamed_energy_efficiency"},
        namespace="EDA"
    )