from flask_jwt_extended import create_access_token, create_refresh_token

def generate_tokens(user):
  # create access token
  access_token = create_access_token(
    identity={ 'id': user.id, 'username': user.username },
    fresh=True,
  )
  # create refresh token
  refresh_token = create_refresh_token(
    identity={ 'id': user.id, 'username': user.username },
  )

  return (access_token, refresh_token)
