"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1) Primer nodo, lecture de datos 
def load_data(filepath: str) -> pd.DataFrame:
    dataset = pd.read_excel(filepath) 
    return dataset # Retorno el set de datos leido  

# 2) Rename columns 
def rename_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset = dataset.copy()
    dataset.rename(columns={
        "X1": "Relative_Compactness",
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
    return dataset # Retorno un set de datos nenombrado 


# 3) Get data shape 
def get_data_shape(dataset: pd.DataFrame) -> pd.DataFrame:
    shape = {
        "Cantidad de columnas": [dataset.shape[1]],
        "Cantidad de filas": [dataset.shape[0]]
    }
    return pd.DataFrame(data=shape) # Regresa un pandas DF con el shape del set de datos 
