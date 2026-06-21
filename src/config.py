import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "churn.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoders.pkl")
DB_PATH = os.path.join(BASE_DIR, "database", "users.db")