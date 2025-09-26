# src/recommender.py
import json
import os

CATALOG_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "catalog.json")

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        # fallback: tiny in-memory catalog
        return [
            {"id": 1, "name": "Nike Shoes", "category": "Shoes", "popularity": 90},
            {"id": 2, "name": "Adidas Socks", "category": "Shoes", "popularity": 70},
            {"id": 3, "name": "Sports Cap", "category": "Accessories", "popularity": 80},
            {"id": 4, "name": "Puma Sneakers", "category": "Shoes", "popularity": 85},
            {"id": 5, "name": "Backpack", "category": "Accessories", "popularity": 95}
        ]
    with open(CATALOG_PATH) as f:
        return json.load(f)

catalog = load_catalog()

def recommend_products(abandoned_items, top_n=3):
    recommendations = []
    for item in abandoned_items:
        # try to find category
        found = next((p for p in catalog if p["name"].lower() == item.lower()), None)
        if found:
            category = found["category"]
            similar = [p for p in catalog if p["category"] == category and p["name"].lower() != item.lower()]
            similar_sorted = sorted(similar, key=lambda x: x["popularity"], reverse=True)
            recommendations.extend(similar_sorted)
    # fallback: top popular items
    if not recommendations:
        popular = sorted(catalog, key=lambda x: x["popularity"], reverse=True)
        recommendations = popular
    # dedupe and return names
    names = []
    for p in recommendations:
        if p["name"] not in names:
            names.append(p["name"])
        if len(names) >= top_n:
            break
    return names
