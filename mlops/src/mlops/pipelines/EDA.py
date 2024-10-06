##################                  ANALISIS EXPLORATORIO DE DATOS                ########################
# En este script se definiran algunas de las funciones que se utilizaran en el análisis exploratorio de datos
import pandas as pd
from kedro.pipeline import node



# 1) Función de boxplots, toma un pandas DF  y una lista para generar secuencialmente una serie de boxplots
def boxplot(dataset:pd.DataFrame, columns:list):
    # Importación de librería necesaria
    import matplotlib.pyplot as plt

    # Inicio del ciclo de impresiones
    for i in columns:
        dataset[i].plot(kind="box")
        plt.title(f"Boxplot de {i}")  # Agrega el título
        plt.show()  # Muestra cada gráfico de manera correcta

# 1.1) Declarar esta funcion como un nodo
boxplot_node  = node(func=boxplot,
                     inputs=["dataset", "params:columns_to_plot"],
                     outputs=None, # No estamos devolviendo nada en este caso, solo se visualiza
                     name="boxplot_node"
                     )


