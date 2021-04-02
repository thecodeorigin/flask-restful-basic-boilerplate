import sqlite3

from flask_restful import Resource, reqparse
from bcrypt import hashpw, gensalt
from flask_jwt_extended import jwt_required, get_jwt

from ..models.role import RoleModel
from ...common.constants.exceptions import NotFoundException


class RoleWithIdParam(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'name',
    type=str,
    required=True,
    help='You need to parse this field'
  )

  def get(self, _id):
    role = RoleModel.find_by_id_or_fail(_id)
    
    return { 'data': role.toDict() }

  def patch(self, _id):
    role = RoleModel.find_by_id_or_fail(_id)
    body = RoleWithIdParam.parser.parse_args()

    role.name = body['name']
    role.save_to_db()

    return { 'data': role.toDict() }

class RoleGetMany(Resource):
  @jwt_required()
  def get(self):
    roles = [role.toDict() for role in RoleModel.query.all()]
    return { 'data': roles }
