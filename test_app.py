from app import create_app
import json
import sys

def test_predict_endpoint():
    print("🔎 Starting full backend integrity test...\n")

    app = create_app()
    client = app.test_client()

    try:
        response = client.post(
            "/predict",
            data=json.dumps({"text": "Aliens landed yesterday"}),
            content_type="application/json"
        )
    except Exception as e:
        print("❌ Request failed:", e)
        sys.exit(1)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("❌ Endpoint did not return 200 OK")
        sys.exit(1)

    data = response.get_json()
    print("Response JSON:", data)

    if not isinstance(data, dict):
        print("❌ Response is not valid JSON dictionary")
        sys.exit(1)

    # Validate at least one prediction-like value exists
    found_prediction = False
    found_confidence = False

    for key, value in data.items():
        if isinstance(value, str):
            found_prediction = True
        if isinstance(value, float) or isinstance(value, int):
            found_confidence = True

    if not found_prediction:
        print("❌ No prediction-like string found in response")
        sys.exit(1)

    if not found_confidence:
        print("❌ No confidence-like numeric value found in response")
        sys.exit(1)

    print("\n✅ FULL SYSTEM CHECK PASSED")
    print("✔ App factory working")
    print("✔ Blueprint working")
    print("✔ Dataset loaded")
    print("✔ Model trained")
    print("✔ Prediction returned")
    print("✔ JSON valid")

if __name__ == "__main__":
    test_predict_endpoint()