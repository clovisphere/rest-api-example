from flask import Blueprint  # type: ignore

bp = Blueprint("errors", __name__)

from app.errors import handlers  # noqa # isort:skip
