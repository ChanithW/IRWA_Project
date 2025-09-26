# src/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import OfferModel

app = FastAPI(title="Offer Suggestor AI Agent")

# Initialize and load model
offer_model = OfferModel()
offer_model.train_model()  # train first time
offer_model.load_model()   # load saved model

# Pydantic schema for request body
class UserData(BaseModel):
    age: int
    location: str
    abandoned_item: str
    previous_offer: str

@app.post("/offer-suggest")
def suggest_offer(user: UserData):
    user_dict = user.dict()
    
    # Calculate acceptance probability
    prob = offer_model.predict_offer(user_dict)

    # Simple offer logic based on probability
    if prob > 0.7:
        recommended_offer = "15% off"
    elif prob > 0.4:
        recommended_offer = "10% off"
    else:
        recommended_offer = "Free shipping"

    return {
        "user_data": user_dict,
        "acceptance_probability": prob,
        "recommended_offer": recommended_offer
    }
