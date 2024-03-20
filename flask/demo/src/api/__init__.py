from flask import Blueprint

bp = Blueprint("api", __name__)


# The below imports need to be in this particular order
# to avoid Circular Import issue
from src.api.routes import error, farmers, farms  # noqa # isort:skip
from src.api.auth import token_auth  # noqa # isort:skip


@bp.before_request
@token_auth.login_required
def before_request():
    """All routes in this blueprint should be authenticated."""
    pass
