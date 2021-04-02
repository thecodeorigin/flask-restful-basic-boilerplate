from bcrypt import checkpw
from ...database.db import db
from ...common.constants.exceptions import NotFoundException

class UserModel(db.Model):
  # set up attributes for SQLAlchemy
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)

  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  
  username = db.Column(db.String(80))
  password = db.Column(db.String(80))
  

  def __init__(self, _id, role_id , username, password):
    self.id = _id
    self.role_id = role_id
    self.username = username
    self.password = password

  def toDict(self):
    return {
      'id': self.id,
      'role': {
        'id': self.role.id,
        'name': self.role.name,
      },
      'username': self.username,
    }
  
  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

  @classmethod
  def find_by_id_or_fail(cls, _id):
    found = cls.find_by_id(_id)

    if found is None:
      raise NotFoundException

    return found

  @classmethod
  def delete_from_db(cls, user):
    try:
      db.session.delete(user)
    except Exception:
      db.session.rollback()
      return False
    else:
      db.session.commit()
      return True

  def is_correct_password(self, password):
    password_in_bytes = password.encode('ascii')
    hashed_password_in_bytes = self.password.encode('ascii')

    return checkpw(password_in_bytes, hashed_password_in_bytes)

  def save_to_db(self):
    try:
      db.session.add(self)
    except Exception:
      db.session.rollback()
      return False
    else:
      db.session.commit()
      return True
