from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def synchronize_db():
  # db.drop_all()
  db.create_all()
