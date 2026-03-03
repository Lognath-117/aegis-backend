from flask import Blueprint, request, jsonify
from app.ml.model import predict_text
from app.services.external_apis import check_newsapi

api = Blueprint("api", __name__, url_prefix="/api/v1")

@api.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    # Internal ML prediction
    result, confidence = predict_text(text)

    # External API validation
    external_result = check_newsapi(text)

    return jsonify({
        "internal_prediction": result,
        "internal_confidence": confidence,
        "external_newsapi": external_result
    })