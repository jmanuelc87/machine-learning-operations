from fastapi import FastAPI, HTTPException
from fastapi import Request
import joblib
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

    # Retornar el resultado en formato JSON
    return {
        "prediction": prediccion[0]
    }