import requests
from app.core.config import Config

def check_newsapi(text):
    if not Config.NEWS_API_KEY:
        return {"error": "API key missing"}

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": text,
        "apiKey": Config.NEWS_API_KEY,
        "pageSize": 3
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if data.get("status") == "ok":
            return {
                "total_results": data.get("totalResults", 0)
            }
        else:
            return {"error": "NewsAPI error"}

    except Exception as e:
        return {"error": str(e)}