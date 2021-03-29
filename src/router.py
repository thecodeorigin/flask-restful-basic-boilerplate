from flask_restful import Api
from .app.resources.user import UserRegister
from .app.resources.auth import AuthRegister

def setup_router(app):
  api = Api(app)

  api.add_resource(AuthRegister, '/auth/register')
