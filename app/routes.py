from flask import Blueprint, request, jsonify
from .model import predict_text
import requests

api = Blueprint("api", __name__)

EXTERNAL_API_URL = "https://api.example.com/factcheck"  # placeholder


def external_check(text):
    try:
        response = requests.post(EXTERNAL_API_URL, json={"text": text}, timeout=3)
        if response.status_code == 200:
            return response.json()
    except:
        return None


@api.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    # Internal model prediction
    result, confidence = predict_text(text)

    # External API check (optional)
    external_result = external_check(text)

    return jsonify({
        "internal_prediction": result,
        "internal_confidence": confidence,
        "external_verification": external_result
    })
