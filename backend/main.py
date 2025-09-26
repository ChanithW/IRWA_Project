from fastapi import FastAPI
from models import Cart, OfferResponse
from utils import choose_offer, recommend_products, load_offer_history, save_offer_history

app = FastAPI(title="Agentic AI Offer Suggestor")

@app.post("/suggest_offer")
def suggest_offer(cart: Cart):
    # Decide offer dynamically
    offer = choose_offer(cart.cart_value)
    
    # Recommend products
    recommendations = recommend_products(cart.items)
    
    # Return decision
    return {
        "offer": offer,
        "recommendations": recommendations
    }

@app.post("/record_response/{user_id}")
def record_response(user_id: int, response: OfferResponse):
    history = load_offer_history()
    history.append({
        "user_id": user_id,
        "cart_value": response.dict().get("cart_value", 0),
        "offer_given": response.dict().get("offer_given", "Unknown"),
        "user_response": response.user_response
    })
    save_offer_history(history)
    return {"status": "response recorded", "total_records": len(history)}
