import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt

from ..models.user import UserModel
from ..models.role import RoleModel
from ...common.helpers.jwt import TokenGenerator
from ...common.variables.blocklist import BLOCKLIST
from ...common.constants.error_messages import ErrorMessage
from ...common.constants.exceptions import NotFoundException

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

    # find default role
    default_role = RoleModel.find_by_name('USER')
    if default_role is None:
      raise NotFoundException

    user = UserModel(None, default_role.id, **body) # ** is like ... in javascript
    user.save_to_db()

    access_token, refresh_token = TokenGenerator.generate_tokens(user)
    return {
      'access_token': access_token, 
      'refresh_token': refresh_token,
    }, 201


class AuthLogin(Resource):
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
    # get data from parser
    body = self.parser.parse_args()
    # find user in db
    user = UserModel.find_by_username(body['username'])
    
    # check password
    # if user and self.is_correct_password(user.password, body['password']):
    if user and user.is_correct_password(body['password']):
      access_token, refresh_token = TokenGenerator.generate_tokens(user)
      return { 'access_token': access_token, 'refresh_token': refresh_token, }, 200
    
    return { 'message': 'Invalid credentials' }, 401


class AuthLogout(Resource):
  @jwt_required()
  def post(self):
    payload = get_jwt()
    BLOCKLIST.add(payload['jti'])
    
    return { 'message': 'Successfully logged out' }, 200


class TokenRefresh(Resource):
  @jwt_required(refresh=True)
  def post(self):
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)

    return { 'access_token': new_token }, 200
