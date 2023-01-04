import uuid
from flask import request, session
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db

from sqlalchemy.exc import SQLAlchemyError

from models.address import AddressModel
from schemas import AddressSchema


blp = Blueprint("addresses", __name__, description="Operations on addresses")


@blp.route("/addresses")
class Address(MethodView):
    @blp.response(200, AddressSchema(many=True))
    def get(self):
        return AddressModel.query.all()


@blp.route("/address/<string:id>")
class Address(MethodView):
    @blp.response(200, AddressSchema)
    def get(self, id):
        address = AddressModel.query.get(id)
        return address

    def delete(self, id):
        address = AddressModel.query.get(id)
        db.session.delete(address)
        db.session.commit()
        return "address deleted"



@blp.route("/address")
class Address(MethodView):
    @blp.arguments(AddressSchema)
    @blp.response(200, AddressSchema)
    def post(self, address_data):
        address = AddressModel(**address_data)

        db.session.add(address)
        db.session.commit()

        return address
