from fastapi import FastAPI, HTTPException
from fastapi import Request
import joblib
import json
import numpy as np

app = FastAPI()

'''
import xgboost as xgb
model = xgb.XGBRegressor()
model.load_model("./mlops/model/model.pkl")
'''

model = joblib.load('./mlops/model/model.pkl')

@app.post("/predict")
async def predict(request: Request):
    # Obtener el JSON del body de la solicitud
    data = await request.json()
    '''
    body_bytes = await request.body()
    # Decodificar a texto
    body_text = body_bytes.decode("utf-8")
    body_json = json.loads(body_text)
    print(body_text)
    #data = {"Relative_Compactness": 0.5, "Surface_Area": 1.2, "Wall_Area": 0.3, "Roof_Area": 0.8, "Overall_Height_0": 1, "Overall_Height_1": 0, "Orientation_0": 0, "Orientation_1": 1, "Orientation_2": 0, "Glazing_Area_0": 0, "Glazing_Area_1": 1, "Glazing_Area_2": 0, "Glazing_Area_Distribution_0": 0, "Glazing_Area_Distribution_1": 1, "Glazing_Area_Distribution_2": 0}
    data = {"Relative_Compactness":0.5}
    data = body_text
    #data = json.loads(body_text)
    '''

    # Asegurarse de que todas las claves necesarias están en el JSON
    required_features = [
        'Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area',
        'Overall_Height_0', 'Overall_Height_1', 'Orientation_0', 'Orientation_1',
        'Orientation_2', 'Glazing_Area_0', 'Glazing_Area_1', 'Glazing_Area_2',
        'Glazing_Area_Distribution_0', 'Glazing_Area_Distribution_1', 'Glazing_Area_Distribution_2'
    ]
    
    for feature in required_features:
        if feature not in data:
            raise HTTPException(status_code=400, detail=f"Missing feature: {feature}")
    print(type(data))
    # Convertir el JSON en un array numpy con los valores proporcionados
    feature_array = np.array([
        data['Relative_Compactness'],
        data['Surface_Area'],
        data['Wall_Area'],
        data['Roof_Area'],
        data['Overall_Height_0'],
        data['Overall_Height_1'],
        data['Orientation_0'],
        data['Orientation_1'],
        data['Orientation_2'],
        data['Glazing_Area_0'],
        data['Glazing_Area_1'],
        data['Glazing_Area_2'],
        data['Glazing_Area_Distribution_0'],
        data['Glazing_Area_Distribution_1'],
        data['Glazing_Area_Distribution_2']
    ]).reshape(1, -1)  

    

    # Realizar la predicción usando el modelo
    prediccion = model.predict(feature_array)
    print(prediccion[0])
    # Retornar el resultado en formato JSON
    return {"prediction": float(prediccion[0])}