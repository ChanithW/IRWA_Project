# src/train_bandit.py
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.bandit import ContextualBandit
from src.feature_utils import cart_to_features, save_scaler
import joblib
import numpy as np

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_offers.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)

OFFERS = ["5% discount", "Free Shipping", "10% discount", "20% discount"]

def build_feature_matrix(df):
    X_list = []
    y_by_offer = {o: [] for o in OFFERS}
    # We'll store corresponding X rows for each offer
    X_rows_by_offer = {o: [] for o in OFFERS}
    for _, r in df.iterrows():
        items = r["items"].split("|") if isinstance(r["items"], str) else []
        x = cart_to_features(r["cart_value"], items, user_history_count=int(r["user_history"]), time_of_day=r["time_of_day"])
        X_list.append(x.ravel())
        offer = r["offer_shown"]
        reward = int(r["reward"])
        X_rows_by_offer[offer].append(x.ravel())
        y_by_offer[offer].append(reward)
    X = np.vstack(X_list)
    return X, X_rows_by_offer, y_by_offer

def main():
    df = pd.read_csv(DATA_PATH)
    bandit = ContextualBandit(OFFERS)
    # Prepare scaler fit on all data
    X, X_rows_by_offer, y_by_offer = build_feature_matrix(df)
    scaler = StandardScaler().fit(X)
    # persist scaler
    save_scaler(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))
    bandit.scaler = scaler

    # Now partial_fit per offer
    for offer in OFFERS:
        X_rows = np.array(X_rows_by_offer[offer])
        y = np.array(y_by_offer[offer])
        if X_rows.shape[0] == 0:
            continue
        # scale features
        X_scaled = scaler.transform(X_rows)
        model = bandit.models[offer]
        # initialize model with classes
        model.partial_fit(X_scaled, y, classes=[0,1])
        model.initialized = True
        # save model
        joblib.dump(model, os.path.join(MODEL_DIR, f"model_{offer.replace(' ', '_')}.pkl"))
        print(f"Trained model for {offer} on {len(y)} samples")

    # save scaler and models
    bandit.save_all()
    print("Training complete. Models saved to", MODEL_DIR)

if __name__ == "__main__":
    main()
