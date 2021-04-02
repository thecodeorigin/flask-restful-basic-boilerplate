from ...database.db import db
from ...common.constants.exceptions import NotFoundException

class RoleModel(db.Model):
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))

  users = db.relationship('UserModel', backref='role')

  def __init__(self, _id, name):
    self.id = _id
    self.name = name

  def toDict(self):
    return {
      'id': self.id,
      'name': self.name,
      'users': [user.toDict() for user in self.users],
    }
  
  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()
  
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
  def delete_from_db(cls, role):
    try:
      db.session.delete(role)
    except Exception:
      db.session.rollback()
      return False
    else:
      db.session.commit()
      return True

  def save_to_db(self):
    try:
      db.session.add(self)
    except Exception:
      db.session.rollback()
      return False
    else:
      db.session.commit()
      return True
