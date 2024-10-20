"""
This is a boilerplate pipeline 'data_transformation'
generated using Kedro 0.19.9
"""



#######################                 DATA TRANFORMATION                   ####################

# Importación de librerias 
from sklearn.model_selection import train_test_split
import os
import pandas as pd 
from sklearn.preprocessing import StandardScaler


# Definición de función de exportación de datos 
def exportacion (dataset: pd.DataFrame, file_name:str, path:str): 

    # Obtención del directorio base, es la dirección base del proyecto 
    root_path = os.getcwd()
        
    # Definir la ruta de exportación, en la ejecución 
    export_path = root_path +  path  
    print ("Root_path:", root_path)
    print ("Export_path:", export_path)

    
    # Comprobar si la carpeta existe, y si no, crearla
    if not os.path.exists(export_path):
        os.makedirs(export_path)
    
    # Exportación 
    dataset.to_excel(
    excel_writer= export_path + f"/{file_name}.xlsx",  # Path and name of the output file
    sheet_name='Sheet1',          
    index=False) 


# 1) Lecture de datos 
def load_data(filepath: str) -> pd.DataFrame:
    dataset = pd.read_excel(filepath) 
    return dataset # Retorno el set de datos leido  

# 2) Rename columns 
def rename_columns(dataset: pd.DataFrame) -> pd.DataFrame:
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
    
    
# 2) Split de datos 
def data_split(dataset:pd.DataFrame) -> pd.DataFrame:
    
    features = dataset.drop(columns=["Heating Load", "Cooling Load"])

    # 1.2) Aislamiento de las variables objetivo 
    cooling_target = dataset[["Cooling Load"]]
    heating_target = dataset[["Heating Load"]]

    # 1.3) Segregación para el cooling 
    X_train, X_test, cooling_train, cooling_test = train_test_split(features, cooling_target, test_size=0.2, random_state=42)

    # 1.4) Segregación para el heating 
    X_train, X_test, heating_train, heating_test = train_test_split(features, heating_target, test_size=0.2, random_state=42)
    
    # 1.5) Exportación de resultados 
    exportacion (dataset = X_train,  file_name = "X_train", path = "/data/03_primary") # exportación de X_train 
    exportacion (dataset = X_test,  file_name = "X_test", path = "/data/03_primary") # exportación de X_train 
    exportacion (dataset = cooling_train,  file_name = "cooling_train", path = "/data/03_primary") # exportación de X_train 
    exportacion (dataset = cooling_test,  file_name = "cooling_test", path = "/data/03_primary") # exportación de X_train 
    exportacion (dataset = heating_train,  file_name = "heating_train", path = "/data/03_primary") # exportación de X_train 
    exportacion (dataset = heating_test,  file_name = "heating_test", path = "/data/03_primary") # exportación de X_train 
    
    return X_train,  X_test, cooling_train, cooling_test, heating_train, heating_test



# 3) Escalamiento de variables numéricas 
def scaling (dataset:pd.DataFrame) -> pd.DataFrame: 
    # 3.1) Aislamiento de variables numéricas 
    numeric_features = dataset[["Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area"]]

    # 3.2) Importamos el objeto scaler 
    scaler = StandardScaler()

    # 3.3) Relizamos la tranformacion 
    scaled_data = scaler.fit_transform(X=numeric_features)

    # 3.4 Convertir el array escalado en un DataFrame nuevamente, con los mismos nombres de columnas
    scaled_dataset = pd.DataFrame(data=scaled_data, columns=numeric_features.columns)
    
    return scaled_dataset

