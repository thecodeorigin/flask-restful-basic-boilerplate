from traceback import print_exc
from werkzeug.exceptions import HTTPException

from ..common.constants.error_messages import ErrorMessage

def config_error_handlers(app):
  @app.errorhandler(400)
  def bad_request_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.BAD_REQUEST }, 400

  @app.errorhandler(401)
  def unauthorized_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.UNAUTHORIZED }, 401

  @app.errorhandler(403)
  def forbidden_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.FORBIDDEN }, 403

  @app.errorhandler(404)
  def not_found_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.NOT_FOUND }, 404

  @app.errorhandler(409)
  def conflicted_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.CONFLICTED }, 409

  @app.errorhandler(500)
  def internal_server_error_exception_handler(error):
    print_exc()
    return { 'message': ErrorMessage.INTERNAL_SERVER_ERROR }, 500

  @app.errorhandler(Exception)
  def exception_handler(error):
    """
    Default exception catcher
    """
    print_exc()
    return { 'message': ErrorMessage.INTERNAL_SERVER_ERROR }, 500
