import joblib
import numpy as np

def load_model(model_path: str):
    return joblib.load(model_path)

def make_prediction(model, features: list[float]):
    features = np.array(features).reshape(1, -1)
    return model.predict(features)
