from flask_restful import Api
from .app.resources.user import UserRegister

def setup_router(app):
  api = Api(app)

  api.add_resource(UserRegister, '/register')
