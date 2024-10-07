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

# 1) Función de boxplots, toma un pandas DF  y una lista para generar secuencialmente una serie de boxplots
def boxplot(dataset:pd.DataFrame, columns:list):
    # Importación de librería necesaria
    import matplotlib.pyplot as plt

    # Inicio del ciclo de impresiones
    for i in columns:
        dataset[i].plot(kind="box")
        plt.title(f"Boxplot de {i}")  # Agrega el título
        output_path = f"/Users/orlandoandrade/Documents/Maestria en inteligencia artificial aplicada/Materias/3 trimestre/Repositorio/Repositorio grupal/machine-learning-operations/mlops/data/02_intermediate/test{i}.png"
        plt.savefig(output_path)
        plt.close()

    return output_path # Regresa esta imagen



# 1.1) Declarar esta funcion como un nodo




# 2) Renaming columns
def rename(dataset:pd.DataFrame, original_name:list, target_name:list):

    for i, w in zip(original_name, target_name):
        dataset.rename(columns={i: j}, inplace=True)

    return dataset # Devolvemos el set de datos renombrado
