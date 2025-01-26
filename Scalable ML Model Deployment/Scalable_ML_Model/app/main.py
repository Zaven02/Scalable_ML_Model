from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel
import os

# Initialize app
app = FastAPI()

# Load model
MODEL_PATH = "C:/ZAVEN/PROJECTS/Scalable ML Model Deployment/Scalable_ML_Model/model/model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please ensure the pickle file is in the correct path.")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading the model from {MODEL_PATH}: {e}")

# Input data model
class PredictionRequest(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Welcome to the ML Model API"}

@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        features = np.array(data.features).reshape(1, -1)
        prediction = model.predict(features)
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
