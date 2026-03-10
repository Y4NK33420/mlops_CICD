from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris ML API")

# Load model globally
try:
    model = joblib.load('model.pkl')
except Exception as e:
    model = None

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(request: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Ensure model.pkl exists.")
    
    # Needs to match exactly 4 features for the Iris dataset
    if len(request.features) != 4:
        raise HTTPException(status_code=400, detail="Iris dataset requires exactly 4 features.")
        
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)
    
    return {"prediction": int(prediction[0])}

@app.get("/")
def health_check():
    return {"status": "Iris API is running", "model_loaded": model is not None}
