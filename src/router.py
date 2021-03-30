from flask_restful import Api
from .app.resources.auth import AuthRegister, AuthLogin, AuthLogout, TokenRefresh
from .app.resources.user import UserGetMany

def setup_router(app):
  api = Api(app)

  api.add_resource(AuthRegister, '/auth/register')
  api.add_resource(AuthLogin, '/auth/login')
  api.add_resource(AuthLogout, '/auth/logout')
  api.add_resource(TokenRefresh, '/auth/refresh')
  api.add_resource(UserGetMany, '/users')
