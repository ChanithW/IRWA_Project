offer_suggestor/
├─ data/
│ └─ synthetic_offers.csv # synthetic dataset (optional)
├─ models/
│ └─ (saved model files go here)
├─ src/
│ ├─ main.py # FastAPI server (serve & online updates)
│ ├─ bandit.py # Contextual bandit (select + update)
│ ├─ train_bandit.py # Offline training script (initialize models)
│ ├─ recommender.py # product recommendation logic (IR)
│ ├─ feature_utils.py # feature extraction / preprocessing
│ └─ synthetic_data.py # generator to make synthetic dataset
├─ requirements.txt
└─ README.md
