from flask_jwt_extended import JWTManager

def config_jwt(app):
  jwt = JWTManager(app)

  @jwt.additional_claims_loader
  def add_claims(identity):
    # if identity['id'] == 1:
    #   return { 'is_admin': True }
    return { 'is_admin': False }
