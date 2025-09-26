# src/bandit.py
import os
import joblib
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

class ContextualBandit:
    def __init__(self, offers, scaler_path=None, epsilon=0.1):
        """
        offers: list of offer names (arms)
        epsilon: exploration probability
        """
        self.offers = offers
        self.epsilon = epsilon
        self.models = {}  # one model per offer
        # classifier uses partial_fit; we use SGDClassifier(probability via log loss)
        for o in offers:
            self.models[o] = SGDClassifier(loss="log", max_iter=1000, tol=1e-3)
            # We will lazy-initialize with partial_fit for classes [0,1]
            self.models[o].initialized = False

        # Standard scaler for features
        self.scaler = StandardScaler()
        # scaler persisted path
        self.scaler_path = scaler_path or os.path.join(MODEL_DIR, "scaler.pkl")
        # Try load scaler if exists
        if os.path.exists(self.scaler_path):
            try:
                self.scaler = joblib.load(self.scaler_path)
            except:
                pass

    def predict_proba(self, feature_vector):
        """Return dict {offer: prob_of_success}"""
        x = feature_vector
        if hasattr(self.scaler, "mean_"):
            x_scaled = self.scaler.transform(x)
        else:
            x_scaled = x
        probs = {}
        for o, model in self.models.items():
            if getattr(model, "initialized", False):
                # predict_proba not available directly on SGDClassifier unless calibrated;
                # but with loss='log' we can use predict_proba (works in sklearn >=0.24)
                try:
                    p = model.predict_proba(x_scaled)[0][1]
                except Exception:
                    # fallback: decision_function -> sigmoid
                    score = model.decision_function(x_scaled)[0]
                    p = 1.0 / (1.0 + np.exp(-score))
            else:
                p = 0.5  # default neutral prob when model uninitialized
            probs[o] = float(p)
        return probs

    def select_offer(self, feature_vector):
        """Epsilon-greedy selection"""
        # Explore with prob epsilon
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.offers), None  # explored offer
        # Otherwise exploit: pick offer with highest predicted prob
        probs = self.predict_proba(feature_vector)
        chosen = max(probs.items(), key=lambda kv: kv[1])[0]
        return chosen, probs

    def update(self, offer, feature_vector, reward):
        """
        Online update of the model for the selected offer.
        reward: 0 or 1
        """
        x = feature_vector
        # ensure scaler is fitted
        if not hasattr(self.scaler, "mean_"):
            # we can't scale until we have multiple samples - fallback: fit on x
            try:
                self.scaler.fit(x)
                joblib.dump(self.scaler, self.scaler_path)
            except:
                pass
        x_scaled = self.scaler.transform(x) if hasattr(self.scaler, "mean_") else x

        model = self.models[offer]
        # partial_fit expects y and classes on first call
        if not getattr(model, "initialized", False):
            model.partial_fit(x_scaled, [reward], classes=[0,1])
            model.initialized = True
        else:
            model.partial_fit(x_scaled, [reward])

        # persist model
        model_path = os.path.join(MODEL_DIR, f"model_{offer.replace(' ', '_')}.pkl")
        joblib.dump(model, model_path)

    def save_all(self):
        # Save all models and scaler
        for o, model in self.models.items():
            if getattr(model, "initialized", False):
                path = os.path.join(MODEL_DIR, f"model_{o.replace(' ', '_')}.pkl")
                joblib.dump(model, path)
        joblib.dump(self.scaler, self.scaler_path)
