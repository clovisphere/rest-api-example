from typing import Any

from app.api.models.user import User
from app.api.routes.error import error_response
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from flask import g  # type: ignore

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username: str, password: str) -> Any:
    g.user = User.query.filter_by(username=username).first()
    if g.user is None:
        return False
    return g.user.verify_password(password)


@basic_auth.error_handler
def unauthorized(status: int) -> tuple[dict, int]:
    return error_response(status)


@token_auth.verify_token
def verify_auth_token(token: str) -> bool:
    g.user = User.verify_auth_token(token)
    return g.user is not None


@token_auth.error_handler
def unauthorized_token(status: int) -> tuple[dict, int]:
    return error_response(status)
