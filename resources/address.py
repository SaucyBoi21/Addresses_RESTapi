from flask_jwt_extended import jwt_required, get_jwt
from flask import abort, request, session
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db

from sqlalchemy.exc import SQLAlchemyError

from models.address import AddressModel
from schemas import AddressSchema


blp = Blueprint("addresses", __name__, description="Operations on addresses")


@jwt_required()
@blp.route("/addresses")
class Address(MethodView):
    @blp.response(200, AddressSchema(many=True))
    def get(self):
        return AddressModel.query.all()


@jwt_required()
@blp.route("/address/<string:id>")
class Address(MethodView):
    @blp.response(200, AddressSchema)
    def get(self, id):
        address = AddressModel.query.get(id)
        return address

    def delete(self, id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        address = AddressModel.query.get(id)
        db.session.delete(address)
        db.session.commit()
        return "address deleted"


@jwt_required()
@blp.route("/address")
class Address(MethodView):
    @blp.arguments(AddressSchema)
    @blp.response(200, AddressSchema)
    def post(self, address_data):
        address = AddressModel(**address_data)

        db.session.add(address)
        db.session.commit()

        return address
