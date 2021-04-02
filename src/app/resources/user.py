import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt
from flask_jwt_extended import jwt_required, get_jwt

from ..models.user import UserModel


class UserWithIdParam(Resource):
  @jwt_required()
  def get(self, _id):
    user = UserModel.find_by_id_or_fail(_id)

    return { 'data': user.toDict() }


class UserGetMany(Resource):
  @jwt_required()
  def get(self):
    # How to get claims(jwt payload): claims = get_jwt()
    users = [user.toDict() for user in UserModel.query.all()]

    return { 'data': users }
