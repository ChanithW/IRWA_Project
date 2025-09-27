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
    def compare_models(self):
        """
        Train and compare multiple classifiers, printing their metrics for selection.
        """
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.svm import SVC
        from sklearn.neighbors import KNeighborsClassifier

        train, _ = self.load_data()
        train_processed = self.preprocess(train, fit_encoders=True)
        X = train_processed[["age", "location", "abandoned_item", "previous_offer"]]
        y = train_processed["accepted_offer"]

        models = {
            "RandomForest": RandomForestClassifier(),
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "SVM": SVC(),
            "KNN": KNeighborsClassifier(),
            "GradientBoosting": GradientBoostingClassifier()
        }

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            print(f"Model: {name}")
            print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
            print(f"Precision: {precision_score(y_test, y_pred):.4f}")
            print(f"Recall: {recall_score(y_test, y_pred):.4f}")
            print(f"F1: {f1_score(y_test, y_pred):.4f}\n")
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

    def evaluate_model(self):
        """
        Evaluate the trained model on the test set and print accuracy, precision, recall, f1-score.
        """
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        _, test = self.load_data()
        test_processed = self.preprocess(test, fit_encoders=False)
        X_test = test_processed[["age", "location", "abandoned_item", "previous_offer"]]
        y_test = test_processed["accepted_offer"]
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        print(f"Test Accuracy: {acc:.4f}")
        print(f"Test Precision: {prec:.4f}")
        print(f"Test Recall: {rec:.4f}")
        print(f"Test F1 Score: {f1:.4f}")
