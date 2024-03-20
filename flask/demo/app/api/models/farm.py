from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app import db
from app.api.models.mixins import Timestamp


class Farm(db.Model, Timestamp):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    # add/define more columns :-)

    farmer_id: Mapped[int] = mapped_column(ForeignKey("farmer.id"), nullable=False)

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            # add more keys/values :-)
            "farmer_id": self.farmer_id,
        }
