import os

from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

env_path = Path('./') / '.env'
load_dotenv(dotenv_path=env_path)

class ConfigEnv:
  ENV = os.getenv('ENV') or 'development'
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  DEBUG = os.getenv('DEBUG') == 'True'
  PORT = os.getenv('PORT') or 5000

  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or False

  JWT_AUTH_HEADER_PREFIX = os.getenv('JWT_AUTH_HEADER_PREFIX') or 'Bearer'
  JWT_REQUIRED_CLAIMS = os.getenv('JWT_REQUIRED_CLAIMS') or [] # Replace default attributes: ['exp', 'iat', 'nbf']
  JWT_ACCESS_TOKEN_EXPIRES = os.getenv('JWT_ACCESS_TOKEN_EXPIRES') or timedelta(hours=1)
  JWT_REFRESH_TOKEN_EXPIRES = os.getenv('JWT_REFRESH_TOKEN_EXPIRES') or timedelta(days=30)
  JWT_BLACKLIST_ENABLED = os.getenv('JWT_BLACKLIST_ENABLED') == 'True'
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


def config_env(app):
  app.config.update(
    ENV = ConfigEnv.ENV,
    JWT_SECRET_KEY = ConfigEnv.JWT_SECRET_KEY,
    SQLALCHEMY_DATABASE_URI = ConfigEnv.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS = ConfigEnv.SQLALCHEMY_TRACK_MODIFICATIONS,
    JWT_AUTH_HEADER_PREFIX = ConfigEnv.JWT_AUTH_HEADER_PREFIX,
    JWT_REQUIRED_CLAIMS = ConfigEnv.JWT_REQUIRED_CLAIMS,
    JWT_ACCESS_TOKEN_EXPIRES = ConfigEnv.JWT_ACCESS_TOKEN_EXPIRES,
    JWT_REFRESH_TOKEN_EXPIRES = ConfigEnv.JWT_REFRESH_TOKEN_EXPIRES,
    JWT_BLACKLIST_ENABLED = ConfigEnv.JWT_BLACKLIST_ENABLED,
    JWT_BLACKLIST_TOKEN_CHECKS = ConfigEnv.JWT_BLACKLIST_TOKEN_CHECKS,
  )
