from flask_restful import Api
from .app.resources.user import UserRegister

def setup_router(appRef):
  api = Api(appRef)

  api.add_resource(UserRegister, '/register')
