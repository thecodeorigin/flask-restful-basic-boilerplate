from ..constants.exceptions import BadRequestException, UnauthorizedException, ForbiddenException, NotFoundException, ConflictedException, InternalServerErrorException

errors = {
  'BadRequestException': { 'status': 400 },
  'UnauthorizedException': { 'status': 401 },
  'ForbiddenException': { 'status': 403 },
  'NotFoundException': { 'status': 404 },
  'ConflictedException': { 'status': 409 },
  'InternalServerErrorException': { 'status': 500 },
}
