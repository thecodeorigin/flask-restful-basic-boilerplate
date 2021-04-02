from werkzeug.exceptions import HTTPException
from traceback import print_exc

from .error_messages import ErrorMessage


class BadRequestException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 400

    if description is None:
      self.description = ErrorMessage.BAD_REQUEST

    super().__init__(description=description, response=response)


class UnauthorizedException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 401

    if description is None:
      self.description = ErrorMessage.UNAUTHORIZED

    super().__init__(description=description, response=response)


class ForbiddenException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 403

    if description is None:
      self.description = ErrorMessage.FORBIDDEN

    super().__init__(description=description, response=response)


class NotFoundException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 404

    if description is None:
      self.description = ErrorMessage.NOT_FOUND

    super().__init__(description=description, response=response)


class ConflictedException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 409

    if description is None:
      self.description = ErrorMessage.CONFLICTED

    super().__init__(description=description, response=response)


class InternalServerErrorException(HTTPException):
  def __init__(self, description=None, response=None):
    self.code = 500

    if description is None:
      self.description = ErrorMessage.INTERNAL_SERVER_ERROR

    super().__init__(description=description, response=response)

