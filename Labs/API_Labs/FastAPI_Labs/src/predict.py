import joblib

model = joblib.load("../model/wine_model.pkl")
def predict_data(X):
    y_pred = model.predict(X)
    return y_pred

def predict_confidence(X):
    if model is None:
        raise Exception("Model is not loaded")
    
    probabilities = model.predict_proba(X)
    return probabilities[0]
