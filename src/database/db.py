from flask_sqlalchemy import SQLAlchemy
from src.config.env import ConfigEnv

db = SQLAlchemy()

def synchronize_db():
  # db.drop_all()
  db.create_all()
