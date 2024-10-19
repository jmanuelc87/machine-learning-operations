"""
This is a boilerplate pipeline 'data_transformation'
generated using Kedro 0.19.9
"""



#######################                 DATA TRANFORMATION                   ####################

# Importación de librerias 
from sklearn.model_selection import train_test_split
import os

# Definición de función de exportación de datos 
def exportacion (dataset: pd.DataFrame, file_name:str, path:str): 

    # Obtención del directorio base, es la dirección base del proyecto 
    root_path = os.getcwd()
    
    # Definir la ruta de exportación, en la ejecución 
    export_path = root_path +  path  
    
    # Comprobar si la carpeta existe, y si no, crearla
    if not os.path.exists(export_path):
        os.makedirs(export_path)
    
    # Exportación 
    dataset.to_excel(
    excel_writer=export_path + f"{file_name}/.xlsx",  # Path and name of the output file
    sheet_name='Sheet1',          
    index=False) 


# 1) Split de datos 

def data_split (dataset:pd.DataFrame) -> pd.DataFrame  
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
    
    
    return X_train,  X_test, cooling_train, cooling_test, heating_train, heating_test