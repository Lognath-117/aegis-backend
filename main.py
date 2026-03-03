from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
CORS(app)

# ----------------------------
# Dummy Training Data
# ----------------------------
texts = [
    "Government announces new economic policy",
    "Aliens landed in New York yesterday",
    "Stock market reaches record high",
    "Drinking bleach cures diseases"
]

labels = [1, 0, 1, 0]  # 1 = Real, 0 = Fake

# ----------------------------
# Train Simple Model
# ----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)


# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def home():
    return "AEGIS Backend Running (Iteration 1)"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]
    confidence = model.predict_proba(transformed_text)[0].max()

    result = "Real" if prediction == 1 else "Fake"

    return jsonify({
        "prediction": result,
        "confidence": round(float(confidence), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
