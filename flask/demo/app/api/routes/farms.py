from app.api import bp as api
from app.api.models.farm import Farm

from flask import jsonify


@api.route("/farms/<int:id>", methods=["GET"])
def get_farm(id: int):
    return Farm.query.get_or_404(id).to_json()


@api.route("/farms", methods=["GET"])
def get_farms():
    farms = Farm.query.all()
    return jsonify([farm.to_json() for farm in farms])


@api.route("/farms", methods=["POST"])
def create_farm():
    pass


@api.route("/farms/<int:id>", methods=["PUT"])
def update_farm(id: int):
    pass
