from flask import Blueprint, request, jsonify
from .model import predict_text

api = Blueprint("api", __name__)

@api.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    result, confidence = predict_text(text)

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })
