import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt
from flask_jwt_extended import jwt_required, get_jwt

from ..models.role import RoleModel


class RoleWithIdParam(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'id',
    type=int,
    required=True,
    help='You need to parse the Id'
  )

  def get(self, _id):
    role = RoleModel.find_by_id(_id)

    if role is None:
      return {
        'error': 'not_found',
        'message': 'Resource not found'
      }
    
    return { 'data': role.toDict() }


class RoleGetMany(Resource):
  @jwt_required()
  def get(self):
    roles = [role.toDict() for role in RoleModel.query.all()]
    return { 'data': roles }
