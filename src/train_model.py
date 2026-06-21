import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("data/churn.csv")

# Remove customerID if present
if "customerID" in df.columns:
    df = df.drop("customerID", axis=1)

# Convert TotalCharges to numeric
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

# Fill missing values
df.fillna(0, inplace=True)

# Encode categorical columns
label_encoders = {}

categorical_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for col in categorical_columns:

    df[col] = df[col].astype(str).str.strip()

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

# Verify encoding
print("\nDATA TYPES AFTER ENCODING:\n")
print(df.dtypes)

# Split Data
X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy: {accuracy:.4f}")

# Save Model
joblib.dump(
    model,
    "models/churn_model.pkl"
)

joblib.dump(
    label_encoders,
    "models/label_encoders.pkl"
)

print("\nModel Saved Successfully")