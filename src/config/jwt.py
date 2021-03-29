from flask_jwt_extended import JWTManager

def config_jwt(app):
  jwt = JWTManager(app)