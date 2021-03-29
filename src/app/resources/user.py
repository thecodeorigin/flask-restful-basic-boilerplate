import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt
from flask_jwt_extended import jwt_required

from ..models.user import UserModel

class UserGetMany(Resource):
  @jwt_required()
  def get(self):
    users = [user.toDict() for user in UserModel.query.all()]

    return { 'data': users }
