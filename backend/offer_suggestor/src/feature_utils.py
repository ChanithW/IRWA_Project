# src/feature_utils.py
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# You may extend categories as your catalog grows
CATEGORY_LIST = ["Shoes", "Accessories", "Clothing", "Electronics", "Home"]

def cart_to_features(cart_value: float, items: list, user_history_count: int = 0, time_of_day: str = "afternoon"):
    """
    Build a simple numeric feature vector from the cart data.
    Features:
      - cart_value (float)
      - num_items (int)
      - avg_item_popularity (we'll accept precomputed popularity or 0)
      - user_history_count (int)  # how many previous purchases
      - time_of_day bucket (one-hot)
      - category bag-of-words for CATEGORY_LIST (counts)
    """
    # Basic numeric features
    num_items = len(items)
    # If items come as dicts with popularity, pass popularity via recommender or prepare separately
    avg_popularity = 0.0
    # Simple time bucket mapping
    time_buckets = ["morning", "afternoon", "evening", "night"]
    time_vec = [1 if time_of_day == t else 0 for t in time_buckets]

    # category counts: items expected to be strings; you should pass category names or product names
    # For simplicity, we check if any CATEGORY_LIST name appears in item string
    cat_counts = []
    for cat in CATEGORY_LIST:
        cnt = sum(1 for it in items if cat.lower() in it.lower())
        cat_counts.append(cnt)

    raw = [cart_value, num_items, avg_popularity, user_history_count] + time_vec + cat_counts
    return np.array(raw, dtype=float).reshape(1, -1)


def save_scaler(scaler: StandardScaler, path):
    joblib.dump(scaler, path)


def load_scaler(path):
    return joblib.load(path)
