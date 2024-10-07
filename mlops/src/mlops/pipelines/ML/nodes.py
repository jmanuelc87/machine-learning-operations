"""
This is a boilerplate pipeline 'ML'
generated using Kedro 0.19.8
"""


##################                  ANALISIS EXPLORATORIO DE DATOS                ########################
# En este script se definiran algunas de las funciones que se utilizaran en el análisis exploratorio de datos
import pandas as pd
from kedro.pipeline import node
import os



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
def boxplot_node(dataset:pd.DataFrame):

    # Importación de librería necesaria
    import matplotlib.pyplot as plt
    import os

    # Obtención del directorio base
    root_path = os.getcwd()

    # Obtención de nombre de las columnas
    columns = dataset.columns.tolist()

    # Definir la ruta de exportación:
    graphs_path = root_path + "/data/02_intermediate/graphs"

    # Comprobar si la carpeta existe, y si no, crearla
    if not os.path.exists(graphs_path):
        os.makedirs(graphs_path)

    # Inicio del ciclo de impresiones
    for i in columns:
        dataset[i].plot(kind="box")
        plt.title(f"Boxplot de {i}")  # Agrega el título
        output_path =  graphs_path + f"/Box plot {i}.png"  # Define la ruta completa del archivo
        plt.savefig(output_path)  # Guardar la gráfica en la carpeta "graphs"
        print("Se guardo el siguiente archivo:", output_path)
        plt.close()

# 3) Shape del conjunto de datos




