from typing import Any

from itsdangerous import URLSafeTimedSerializer as TimedSerializer
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app import db
from app.api.models.mixins import Timestamp
from werkzeug.security import check_password_hash, generate_password_hash

from flask import current_app


class User(db.Model, Timestamp):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self) -> str:
        return TimedSerializer(current_app.config["SECRET_KEY"]).dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token, max_age: int = 3600) -> Any:
        s = TimedSerializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token, max_age=max_age)
        except Exception:
            return None
        return User.query.get(data["id"])
