from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

from ..app.models.user import UserModel

def config_jwt(app):
  jwt = JWT(app, authenticate, identity)

  # identity params is what "authenticate" func returns
  @jwt.jwt_payload_handler
  def customized_encode_handler(identity):
    return { 'user_id': identity.id }

def authenticate(username, password):
  user = UserModel.find_by_username(username)

  if user and safe_str_cmp(user.password, password): return user
  return None

def identity(payload):
  user_id = payload['user_id']
  return UserModel.find_by_id(user_id)
