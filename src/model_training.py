import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    label_encoders = {}
    for column in ["Animal Name", "Food Style", "Nature", "What It Likes Most"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le  # Store for later use
    return df, label_encoders

def train_model(df):
    X = df[["Lifespan (years)", "Food Style"]]
    y = df["Nature"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    return model

def save_model(model, encoders, model_path, encoder_path):
    joblib.dump(model, model_path)
    joblib.dump(encoders, encoder_path)

def main():
    data_path = "data/animal_dataset.csv"
    model_path = "models/trained_model.pkl"
    encoder_path = "models/label_encoders.pkl"
    if not os.path.exists(data_path):
        print("Dataset not found! Please ensure the CSV file exists in the 'data' folder.")
        return
    df, encoders = preprocess_data(data_path)
    model = train_model(df)
    save_model(model, encoders, model_path, encoder_path)
    print("Model training complete. Model saved in 'models/' folder.")

if __name__ == "__main__":
    main()
