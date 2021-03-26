import os

from flask import Flask
from flask_restful import Api

from src.config.env import config_env
from src.database.db import db, synchronize_db
from src.config.env import ConfigEnv
from src.config.jwt import config_jwt
from src.router import setup_router

app = Flask(__name__)
config_env(app)
config_jwt(app)

setup_router(app)

@app.before_first_request
def synchronize_database():
  if ConfigEnv.ENV == 'development':
    synchronize_db()

if __name__ == '__main__':
  db.init_app(app)

  app.run(port=5001, debug=ConfigEnv.DEBUG)