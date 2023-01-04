from marshmallow import Schema, fields


class AddressSchema(Schema):
    id = fields.Int(dump_only=True)
    country = fields.Str(required=True)
    state = fields.Str(required=True)
    city = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    street = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)