from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import joblib

# Load models
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

def analyze_text_emotion(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    return torch.argmax(logits, dim=1).item()  # Return the predicted class index

# Load LightGBM model and vectorizer
model_lgb = joblib.load("models/lightgbm_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_emotion(text):
    lgb_vectorized = vectorizer.transform([text])
    lgb_prediction = model_lgb.predict(lgb_vectorized)
    return lgb_prediction[0]  # Return the first prediction
