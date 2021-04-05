from flask_jwt_extended import create_access_token, create_refresh_token

class TokenGenerator:
  @classmethod
  def generate_tokens(cls, user):
    # create access token
    access_token = create_access_token(
      identity={ 'id': user.id, 'username': user.username, 'role_id': user.role_id },
      fresh=True,
    )
    # create refresh token
    refresh_token = create_refresh_token(
      identity={ 'id': user.id, 'username': user.username },
    )

    return (access_token, refresh_token)
