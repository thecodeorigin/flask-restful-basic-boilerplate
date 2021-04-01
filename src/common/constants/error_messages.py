class ErrorMessage:
  # HTTP
  BAD_REQUEST = 'Bad Request'
  UNAUTHORIZED = 'Unauthorized'
  FORBIDDEN = 'Forbidden Resource'
  NOT_FOUND = 'Resource Not Found'
  CONFLICTED = 'Conflicted'
  DUPLICATED = 'Duplicated Entry'
  INTERNAL_SERVER_ERROR = 'Internal Server Error'
  # JWT
  TOKEN_EXPIRED = 'The token has expired'
  INVALID_TOKEN = 'Token verification failed'
  FRESH_TOKEN_REQUIRED = 'The token is not fresh'
  TOKEN_REVOKED = 'The token has been revoked'
  # OTHERS
  INVALID_ENTRY = 'Invalid Entry'
  INVALID_CREDENTIALS = 'Invalid Credentials'
