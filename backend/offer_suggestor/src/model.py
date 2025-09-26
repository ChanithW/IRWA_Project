# src/model.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

MODEL_PATH = os.path.join(DATA_DIR, "offer_model.pkl")
ENCODER_PATH = os.path.join(DATA_DIR, "encoders.pkl")

class OfferModel:
    def __init__(self):
        self.model = None
        self.encoders = {}

    def load_data(self):
        train = pd.read_csv(os.path.join(DATA_DIR, "offers_train.csv"))
        test = pd.read_csv(os.path.join(DATA_DIR, "offers_test.csv"))
        return train, test

    def preprocess(self, df, fit_encoders=False):
        df_copy = df.copy()
        for col in ["location", "abandoned_item", "previous_offer"]:
            if fit_encoders:
                le = LabelEncoder()
                df_copy[col] = le.fit_transform(df_copy[col])
                self.encoders[col] = le
            else:
                le = self.encoders[col]
                df_copy[col] = le.transform(df_copy[col])
        # Convert Yes/No to 1/0 for label
        if "accepted_offer" in df_copy.columns:
            df_copy["accepted_offer"] = df_copy["accepted_offer"].map({"Yes":1, "No":0})
        return df_copy

    def train_model(self):
        train, test = self.load_data()
        train_processed = self.preprocess(train, fit_encoders=True)

        X_train = train_processed[["age", "location", "abandoned_item", "previous_offer"]]
        y_train = train_processed["accepted_offer"]

        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Save model and encoders
        pickle.dump(self.model, open(MODEL_PATH, "wb"))
        pickle.dump(self.encoders, open(ENCODER_PATH, "wb"))

        print("Model trained and saved!")

    def load_model(self):
        self.model = pickle.load(open(MODEL_PATH, "rb"))
        self.encoders = pickle.load(open(ENCODER_PATH, "rb"))

    def predict_offer(self, user_data):
        """
        user_data = dict with keys: age, location, abandoned_item, previous_offer
        """
        df = pd.DataFrame([user_data])
        for col, le in self.encoders.items():
            df[col] = le.transform(df[col])
        X = df[["age", "location", "abandoned_item", "previous_offer"]]
        prob = self.model.predict_proba(X)[0][1]  # probability of acceptance
        return prob
