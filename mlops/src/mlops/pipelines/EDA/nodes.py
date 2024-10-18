"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""



import pandas as pd
import matplotlib.pyplot as plt
import os

# 1) Primer nodo, lecture de datos 
def load_data(filepath: str) -> pd.DataFrame:
    return pd.read_excel(filepath)



