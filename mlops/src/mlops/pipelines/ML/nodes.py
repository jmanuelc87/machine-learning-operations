"""
This is a boilerplate pipeline 'ML'
generated using Kedro 0.19.8
"""


##################                  ANALISIS EXPLORATORIO DE DATOS                ########################
# En este script se definiran algunas de las funciones que se utilizaran en el análisis exploratorio de datos
import pandas as pd
from kedro.pipeline import node
import os

root_path = os.getcwd()



# 1) Declaración de la función rename
def rename_node(dataset:pd.DataFrame):
    # Modifico directamente el nombre de las columnas
    dataset.rename(columns={"X1": "Relative_Compactness",
                            "X2": "Surface_Area",
                            "X3": "Wall_Area",
                            "X4": "Roof_Area",
                            "X5": "Overall_Height",
                            "X6": "Orientation",
                            "X7": "Glazing Area",
                            "X8": "Glazing Area Distribution",
                            "Y1": "Heating Load",
                            "Y2": "Cooling Load"
                            }, inplace=True)
    return dataset




# 2) Función de boxplots, toma un pandas DF  y una lista para generar secuencialmente una serie de boxplots
def boxplot(dataset:pd.DataFrame, columns:list): # Importante, hay que indicarle
    # Importación de librería necesaria
    import matplotlib.pyplot as plt

    # Inicio del ciclo de impresiones
    for i in columns:
        dataset[i].plot(kind="box")
        plt.title(f"Boxplot de {i}")  # Agrega el título
        output_path = f"/Users/orlandoandrade/Documents/Maestria en inteligencia artificial aplicada/Materias/3 trimestre/Repositorio/Repositorio grupal/machine-learning-operations/mlops/data/02_intermediate/test{i}.png"
        plt.savefig(output_path)
        plt.close()

# 2) Segunda funcion, estoy simoplificando los parametros y dejandolo solo en funcion al set de datos de entrada
def boxplot_node(dataset: pd.DataFrame):
    columns = dataset.columns.tolist()
    boxplot(dataset, columns)



