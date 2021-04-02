from flask_restful import Api

from .app.resources.auth import AuthRegister, AuthLogin, AuthLogout, TokenRefresh
from .app.resources.user import UserWithIdParam, UserGetMany
from .app.resources.role import RoleWithIdParam, RoleGetMany
from .common.variables.errors import errors

def setup_router(app):
  api = Api(app, errors=errors)

  api.add_resource(AuthRegister, '/auth/register')
  api.add_resource(AuthLogin, '/auth/login')
  api.add_resource(AuthLogout, '/auth/logout')
  api.add_resource(TokenRefresh, '/auth/refresh')

  api.add_resource(UserGetMany, '/users')
  api.add_resource(UserWithIdParam, '/users/<int:_id>')

  api.add_resource(RoleGetMany, '/roles')
  api.add_resource(RoleWithIdParam, '/roles/<int:_id>')
