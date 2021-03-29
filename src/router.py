from flask_restful import Api
from .app.resources.auth import AuthRegister, AuthLogin
from .app.resources.user import UserGetMany

def setup_router(app):
  api = Api(app)

  api.add_resource(AuthRegister, '/auth/register')
  api.add_resource(AuthLogin, '/auth/login')
  api.add_resource(UserGetMany, '/users')
