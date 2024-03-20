from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db
from app.api.models.farm import Farm
from app.api.models.mixins import Timestamp


class Farmer(db.Model, Timestamp):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    middle_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    id_number: Mapped[str] = mapped_column(String(30))

    # add/define more columns :-)

    farms: Mapped[list["Farm"]] = relationship(backref="farmer")

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            # add more keys/values :-)
            "farms": [farm.to_json() for farm in self.farms],
        }
