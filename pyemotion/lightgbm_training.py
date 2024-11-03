import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv("data_emotion.csv")
X = data["text"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

lgb_train = lgb.Dataset(X_train_vectorized, label=y_train)
params = {
    "objective": "multiclass",
    "num_class": 5,  # Adjust according to your number of classes
    "metric": "multi_logloss",
}

model_lgb = lgb.train(params, lgb_train)
joblib.dump(model_lgb, "lightgbm_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
