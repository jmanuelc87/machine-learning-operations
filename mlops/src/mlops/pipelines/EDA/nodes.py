"""
This is a boilerplate pipeline 'EDA'
generated using Kedro 0.19.9
"""


#######################                          ANALISIS EXPLORATORIO DE DATOS                  ###########################
                        
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

# 4) Estadistica descriptiva 
def descriptive_statistics (dataset: pd.DataFrame) -> pd.DataFrame: 
    # 4.1) Generamos la estadistica necesaria 
    dataset = dataset.describe(include="number").T
    
    # Meto el indice como una columna 
    dataset["variable"] = dataset.index 
    dataset.reset_index(drop = True, inplace =True)
    
    # 4.2) Exportamos los resultados 
    import os

    # Obtención del directorio base, es la dirección base del proyecto 
    root_path = os.getcwd()
    
    # Definir la ruta de exportación, en la ejecución 
    export_path = root_path + "/data/02_intermediate/EDA"
    
    # Comprobar si la carpeta existe, y si no, crearla
    if not os.path.exists(export_path):
        os.makedirs(export_path)
    
    # Exportación 
    dataset.to_excel(
    excel_writer=export_path + "/estadistica_descriptiva.xlsx",  # Path and name of the output file
    sheet_name='Sheet1',          # Sheet name
    index=False) 

    return dataset 



# 5) Generación de histogramas 
def histograms (dataset:pd.DataFrame): 

    # 5.1) Generación del histogramas
    dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1, figsize=(12,12))

    # 5.2) Save the figure as PNG
    import os

    # Obtención del directorio base, es la dirección base del proyecto 
    root_path = os.getcwd()
    
    # Definir la ruta de exportación, en la ejecución 
    export_path = root_path + "/data/02_intermediate/EDA"
    
    # Comprobar si la carpeta existe, y si no, crearla
    if not os.path.exists(export_path):
        os.makedirs(export_path)
    
    plt.savefig(export_path + "/histograms.png", format="png", dpi=300, bbox_inches='tight')    
    
    return plt