from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from predict import predict_data, predict_confidence
from typing import Dict


app = FastAPI()

class WineData(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

class WineResponse(BaseModel):
    response:int

@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status": "healthy"}

@app.post("/predict", response_model=WineResponse)
async def predict_wine(wine_features: WineData):
    try:
        features = [[wine_features.alcohol, wine_features.malic_acid, wine_features.ash, wine_features.alcalinity_of_ash,
            wine_features.magnesium, wine_features.total_phenols, wine_features.flavanoids, wine_features.nonflavanoid_phenols,
            wine_features.proanthocyanins, wine_features.color_intensity, wine_features.hue, wine_features.od280_od315_of_diluted_wines,
            wine_features.proline]]

        prediction = predict_data(features)
        return WineResponse(response=int(prediction[0]))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class DetailedResponse(BaseModel):
    response: int
    confidence_scores: Dict[str, float]
    top_confidence: float

@app.post("/predict/confidence", response_model=DetailedResponse)
async def predict_wine_confidence(wine_features: WineData):
    try:
        features = [list(wine_features.dict().values())]
        prediction = predict_data(features)[0]
        
        probs = predict_confidence(features)
        
        confidence_dict = {
            "Class 0": round(probs[0], 4), "Class 1": round(probs[1], 4), "Class 2": round(probs[2], 4)
        }

        return DetailedResponse(
            response=int(prediction),
            confidence_scores=confidence_dict,
            top_confidence=round(max(probs), 4)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


    
