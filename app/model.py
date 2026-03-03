from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dummy Training Data
texts = [
    "Government announces new economic policy",
    "Aliens landed in New York yesterday",
    "Stock market reaches record high",
    "Drinking bleach cures diseases"
]

labels = [1, 0, 1, 0]  # 1 = Real, 0 = Fake

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
