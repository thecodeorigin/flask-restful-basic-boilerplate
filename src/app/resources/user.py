import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt

from ..models.user import UserModel
from ...common.constants.roles import RoleConstant
from ...common.decorators.guards import role_guard


class UserWithIdParam(Resource):
  @jwt_required()
  @role_guard([RoleConstant.USER, RoleConstant.ADMIN], get_jwt)
  def get(self, _id):
    user = UserModel.find_by_id_or_fail(_id)

    return { 'data': user.toDict() }


class UserGetMany(Resource):
  @jwt_required()
  @role_guard([RoleConstant.USER, RoleConstant.ADMIN], get_jwt)
  def get(self):
    # How to get claims(jwt payload): claims = get_jwt()
    users = [user.toDict() for user in UserModel.query.all()]

    return { 'data': users }
