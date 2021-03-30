from flask_jwt_extended import JWTManager

from ..common.variables.blocklist import BLOCKLIST
from ..common.constants.error_type import ErrorType

def config_jwt(app):
  jwt = JWTManager(app)

  @jwt.additional_claims_loader
  def add_claims(identity):
    """
    This method will add additional claims (json fields) to the jwt payload.
    @Example { ..., new_claim: 1, ... }
    
    :identity param is the infomation we've been added to the payload, and it
    will be in 'sub' field.
    @Example { ..., sub: { identity_field_1: 1, identity_field_2: 2 }, ... }
    """
    if identity['username'] == 'admin':
      return { 'is_admin': True }
    return { 'is_admin': False }

  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
    """
    This method is called when the token has expired.
    
    :jwt_header & :jwt_payload is the compulsory params for this method,
    they contains header & payload of the expired token.
    """
    return {
      'error': ErrorType.token_expired,
      'message': 'The token has expired',
    }, 401

  @jwt.invalid_token_loader
  def invalid_token_callback(error):
    """
    This method is called when any parts of the token was modified.
    So it raise an error, and handle it here.
    """
    return {
      'error': ErrorType.invalid_token,
      'message': 'Token verification failed',
    }, 401
  
  @jwt.unauthorized_loader
  def unauthorized_callback(error):
    """
    This method is called when client did not 
    send the token in 'Authorization' header
    """
    return {
      'error': ErrorType.unauthorized,
      'message': 'JWT token not provided'
    }, 401

  @jwt.needs_fresh_token_loader
  def needs_fresh_token_callback(jwt_header, jwt_payload):
    """
    This method is called when fresh token
    (token with payload's field 'fresh'=True) is required.
    
    :jwt_header & :jwt_payload is the compulsory params for this method,
    they contains header & payload of the expired token.
    """
    return {
      'error': ErrorType.fresh_token_required,
      'message': 'The token is not fresh'
    }, 401

  @jwt.revoked_token_loader
  def revoked_token_callback(jwt_header, jwt_payload):
    """
    This method is called when the token has been revoked (example: blocklist).
    
    :jwt_header & :jwt_payload is the compulsory params for this method,
    they contains header & payload of the expired token.
    """
    return {
      'error': ErrorType.token_revoked,
      'message': 'The token has been revoked'
    }, 401
  
  @jwt.token_in_blocklist_loader
  def check_if_token_in_blocklist(jwt_header, jwt_payload):
    """
    This method is called whenever a request required a token. It would check
    if the token id was in the blocklist (i.e: logged out), if it does, call revoked callback
    
    :jwt_header & :jwt_payload is the compulsory params for this method,
    they contains header & payload of the expired token.
    """
    return jwt_payload['jti'] in BLOCKLIST
