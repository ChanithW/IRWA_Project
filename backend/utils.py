import json
import random

# Load catalog
with open("catalog.json") as f:
    catalog = json.load(f)

# Load offer history
def load_offer_history():
    try:
        with open("offer_history.json") as f:
            return json.load(f)
    except:
        return []

# Save offer history
def save_offer_history(history):
    with open("offer_history.json", "w") as f:
        json.dump(history, f, indent=4)

# Choose offer probabilistically (contextual bandit simulation)
def choose_offer(cart_value):
    offers = ["5% discount", "Free Shipping", "10% discount", "20% discount"]
    history = load_offer_history()
    
    # Calculate success rates per offer (default = 0.5)
    success_rates = {}
    for offer in offers:
        offer_data = [h["user_response"] for h in history if h["offer_given"] == offer]
        if len(offer_data) > 0:
            success_rates[offer] = sum(offer_data) / len(offer_data)
        else:
            success_rates[offer] = 0.5  # default probability
    
    # Weight offers based on cart value (context)
    if cart_value >= 10000:
        context_multiplier = {"20% discount": 1.5, "10% discount": 1.2}
    elif cart_value >= 7000:
        context_multiplier = {"10% discount": 1.5, "Free Shipping": 1.2}
    elif cart_value >= 5000:
        context_multiplier = {"Free Shipping": 1.5, "5% discount": 1.2}
    else:
        context_multiplier = {"5% discount": 1.5}
    
    # Apply context multiplier
    weights = []
    for offer in offers:
        multiplier = context_multiplier.get(offer, 1)
        weights.append(success_rates[offer] * multiplier)
    
    # Pick offer probabilistically
    chosen_offer = random.choices(offers, weights=weights, k=1)[0]
    return chosen_offer

# Recommend products based on abandoned items
def recommend_products(abandoned_items, top_n=3):
    recommendations = []
    for item in abandoned_items:
        # Find category
        category = None
        for product in catalog:
            if product["name"].lower() == item.lower():
                category = product["category"]
        # Recommend popular items in same category
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
