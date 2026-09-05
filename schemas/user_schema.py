from marshmallow import Schema, fields, validate

class UserSchema(Schema):
  name = fields.Str(
    required=True,
    validate=validate.Length(min=2, max=100)
  )

  email= fields.Email(required=True)