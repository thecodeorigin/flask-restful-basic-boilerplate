import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('./') / '.env'
load_dotenv(dotenv_path=env_path)

class ConfigEnv:
  ENV = os.getenv('ENV') or 'development'
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  DEBUG = os.getenv('DEBUG') == 'True'

  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False

  JWT_AUTH_HEADER_PREFIX = os.getenv('JWT_AUTH_HEADER_PREFIX') or 'Bearer'
   # Replace default attributes: ['exp', 'iat', 'nbf']
  JWT_REQUIRED_CLAIMS = os.getenv('JWT_REQUIRED_CLAIMS') or []


def config_env(app):
  app.config.update(
    ENV = ConfigEnv.ENV,
    JWT_SECRET_KEY = ConfigEnv.JWT_SECRET_KEY,
    SQLALCHEMY_DATABASE_URI = ConfigEnv.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS = ConfigEnv.SQLALCHEMY_TRACK_MODIFICATIONS,
    JWT_AUTH_HEADER_PREFIX = ConfigEnv.JWT_AUTH_HEADER_PREFIX,
    JWT_REQUIRED_CLAIMS = ConfigEnv.JWT_REQUIRED_CLAIMS,
  )
