from flask import Flask
from flask_cors import CORS
from .routes import api

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(api)

    @app.route("/")
    def home():
        return "AEGIS Backend Running (Iteration 2)"

    return app
