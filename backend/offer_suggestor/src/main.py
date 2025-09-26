# src/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import joblib
from src.bandit import ContextualBandit
from src.feature_utils import cart_to_features, load_scaler
from src.recommender import recommend_products

# Offers must match models trained
OFFERS = ["5% discount", "Free Shipping", "10% discount", "20% discount"]
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

app = FastAPI(title="Agentic Offer Suggestor - Contextual Bandit")

# Load scaler if exists
scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")
bandit = ContextualBandit(OFFERS, scaler_path=scaler_path, epsilon=0.1)
# Try to load per-offer models
for o in OFFERS:
    path = os.path.join(MODEL_DIR, f"model_{o.replace(' ', '_')}.pkl")
    if os.path.exists(path):
        try:
            bandit.models[o] = joblib.load(path)
            bandit.models[o].initialized = True
        except Exception as e:
            print("Could not load model", path, e)

class CartIn(BaseModel):
    user_id: int
    cart_value: float
    items: list
    time_of_day: str = "afternoon"
    user_history: int = 0

class RecordResponseIn(BaseModel):
    user_id: int
    offer_shown: str
    reward: int  # 1 or 0
    cart_value: float
    items: list
    time_of_day: str = "afternoon"
    user_history: int = 0

@app.post("/suggest_offer")
def suggest_offer(cart: CartIn):
    # Build features
    x = cart_to_features(cart.cart_value, cart.items, user_history_count=cart.user_history, time_of_day=cart.time_of_day)
    # use bandit to select offer
    chosen, probs = bandit.select_offer(x)
    recommendations = recommend_products(cart.items, top_n=3)
    # Return chosen offer + probabilities for explainability + recs
    return {
        "offer": chosen,
        "probabilities": probs,
        "recommendations": recommendations
    }

@app.post("/record_response")
def record_response(r: RecordResponseIn):
    if r.offer_shown not in OFFERS:
        raise HTTPException(status_code=400, detail="Unknown offer")
    x = cart_to_features(r.cart_value, r.items, user_history_count=r.user_history, time_of_day=r.time_of_day)
    # Update the bandit model for the shown offer
    bandit.update(r.offer_shown, x, int(r.reward))
    # Optionally persist models now
    bandit.save_all()
    return {"status": "updated", "offer": r.offer_shown, "reward": r.reward}
