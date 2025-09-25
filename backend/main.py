'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define what the client sends (cart info)
class Cart(BaseModel):
    cart_value: float

@app.post("/suggest_offer")
def suggest_offer(cart: Cart):
    if cart.cart_value >= 10000:
        return {"offer": "20% discount"}
    elif cart.cart_value >= 5000:
        return {"offer": "Free Shipping"}
    else:
        return {"offer": "5% discount"}
'''


from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

app = FastAPI(title="Offer Suggestor Agentic AI Demo")

# Load product catalog
with open("catalog.json") as f:
    catalog = json.load(f)

# Simulated past offer success table
offer_success = {
    "5% discount": {"success": 0.3},
    "Free Shipping": {"success": 0.5},
    "10% discount": {"success": 0.6},
    "20% discount": {"success": 0.7}
}

# Input model
class Cart(BaseModel):
    cart_value: float
    items: list

# Helper: choose offer (simulate learning/agentic)
def choose_offer(cart_value):
    if cart_value >= 10000:
        return "20% discount"
    elif cart_value >= 7000:
        return "10% discount"
    elif cart_value >= 5000:
        return "Free Shipping"
    else:
        return "5% discount"

# Helper: recommend products (simple IR)
def recommend_products(abandoned_items, top_n=3):
    recommendations = []
    for item in abandoned_items:
        # Find similar category products
        category = None
        for product in catalog:
            if product["name"].lower() == item.lower():
                category = product["category"]
        # Pick top popular products from same category
        if category:
            similar = [p for p in catalog if p["category"] == category and p["name"].lower() not in [i.lower() for i in abandoned_items]]
            similar_sorted = sorted(similar, key=lambda x: x["popularity"], reverse=True)
            recommendations.extend(similar_sorted)
    # Remove duplicates & limit top_n
    unique_recs = []
    names = set()
    for p in recommendations:
        if p["name"] not in names:
            unique_recs.append(p)
            names.add(p["name"])
        if len(unique_recs) >= top_n:
            break
    return [p["name"] for p in unique_recs]

# API endpoint
@app.post("/suggest_offer")
def suggest_offer(cart: Cart):
    offer = choose_offer(cart.cart_value)
    recommendations = recommend_products(cart.items)
    # Return agent decision
    return {
        "offer": offer,
        "recommendations": recommendations
    }
