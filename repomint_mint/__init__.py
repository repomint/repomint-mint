from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config


__version__ = "0.1.0"


jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    jwt.init_app(app)

    from repomint_mint.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
