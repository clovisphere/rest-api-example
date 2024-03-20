from typing import Any

from app.api import bp
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code: int, message: str | None = None) -> tuple[dict, int]:
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}
    if message:
        payload["message"] = message
    return payload, status_code


def bad_request(message: str) -> tuple[dict, int]:
    return error_response(400, message)


@bp.errorhandler(HTTPException)  # type: ignore
def handle_exception(e: Any) -> tuple[dict, int]:
    return error_response(e.code)
