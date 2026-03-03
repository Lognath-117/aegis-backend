import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "../data/dataset.json")

with open(dataset_path, "r") as f:
    data = json.load(f)

texts = data["texts"]
labels = data["labels"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_text(text):
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]
    confidence = model.predict_proba(transformed_text)[0].max()

    result = "Real" if prediction == 1 else "Fake"
    return result, round(float(confidence), 2)