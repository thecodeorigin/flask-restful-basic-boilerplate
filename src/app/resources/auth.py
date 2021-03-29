import sqlite3
from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt

from ..models.user import UserModel

class AuthRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'username',
    type=str,
    required=True,
    help='This field cannot be left blank'
  )
  parser.add_argument(
    'password',
    type=str,
    required=True,
    help='This field cannot be left blank'
  )

  def post(self):
    body = AuthRegister.parser.parse_args()

    if UserModel.find_by_username(body['username']):
      return { 'message': 'A user with that username already exists' }, 400

    # hash password
    password_in_bytes = body['password'].encode('ascii')
    body['password'] = hashpw(password_in_bytes, gensalt())

    user = UserModel(None, **body) # ** is like ... in javascript
    user.save_to_db()

    return { 'message': 'User created successfully' }, 201