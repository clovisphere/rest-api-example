from app.api import bp as api
from app.api.models.farmer import Farmer

from flask import jsonify  # type: ignore


@api.route("/farmers/<int:id>", methods=["GET"])
def get_farmer(id: int):
    return Farmer.query.get_or_404(id).to_json()


@api.route("/farmers", methods=["GET"])
def get_farmers():
    farmers = Farmer.query.all()
    return jsonify([farmer.to_json() for farmer in farmers])


@api.route("/farmers", methods=["POST"])
def create_farmer():
    pass


@api.route("/farmers/<int:id>", methods=["PUT"])
def update_farmer(id: int):
    pass
