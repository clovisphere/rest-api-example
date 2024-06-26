from typing import Any

from config.db import Base
from config.default import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from flask import Flask, g  # type: ignore

db = SQLAlchemy(model_class=Base)


def create_app(config_name: str) -> Any:
    """Create an application instance."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    # basic health check 🌡️ 😽
    @app.route("/health", methods=["GET"])
    def health() -> tuple[dict[str, str], int]:
        response, status = {"status": "healthy"}, 200
        try:
            db.session.execute(text("SELECT 1"))
        except Exception:
            response["status"] = "unhealthy"
            status = 500
        return response, status

    # define a token generation route
    from app.api.auth import basic_auth

    @app.route("/get-auth-token", methods=["GET"])
    @basic_auth.login_required
    def get_auth_token() -> dict:
        return {"token": g.user.generate_auth_token()}

    # register blueprints
    from app.api import bp as api_bp
    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    return app
