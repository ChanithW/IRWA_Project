# src/synthetic_data.py
import random
import csv
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_offers.csv")

OFFERS = ["5% discount", "Free Shipping", "10% discount", "20% discount"]
CATEGORIES = ["Shoes", "Accessories", "Clothing", "Electronics", "Home"]
ITEMS = {
    "Shoes": ["Nike Shoes", "Puma Sneakers", "Adidas Running Shoes"],
    "Accessories": ["Backpack", "Sports Cap", "Wristband"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket"],
    "Electronics": ["Phone Case", "Earbuds"],
    "Home": ["Coffee Mug", "Cushion"]
}

def gen_row(user_id):
    num_items = random.choices([1,2,3], [0.6,0.3,0.1])[0]
    cats = random.choices(CATEGORIES, k=num_items)
    items = [random.choice(ITEMS[c]) for c in cats]
    cart_value = round(sum(random.uniform(20, 200) for _ in items) * 50, 2)  # currency-like
    time_of_day = random.choice(["morning", "afternoon", "evening", "night"])
    user_history = random.randint(0, 10)
    # choose an offer to simulate shown
    offer = random.choices(OFFERS, weights=[0.2,0.3,0.3,0.2])[0]
    # Simulate reward probabilistically: higher discounts more likely to convert on high cart_value
    base = 0.05
    if offer == "5% discount":
        prob = 0.05 + min(0.2, cart_value / 20000)
    elif offer == "Free Shipping":
        prob = 0.08 + min(0.25, cart_value / 25000)
    elif offer == "10% discount":
        prob = 0.12 + min(0.35, cart_value / 15000)
    else:
        prob = 0.18 + min(0.45, cart_value / 12000)
    reward = 1 if random.random() < prob else 0
    return {
        "user_id": user_id,
        "cart_value": cart_value,
        "items": "|".join(items),
        "time_of_day": time_of_day,
        "user_history": user_history,
        "offer_shown": offer,
        "reward": reward
    }

def generate(n=5000):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames=["user_id","cart_value","items","time_of_day","user_history","offer_shown","reward"])
        writer.writeheader()
        for uid in range(1, n+1):
            writer.writerow(gen_row(uid))
    print("Saved synthetic data to", OUT)

if __name__ == "__main__":
    generate(10000)
