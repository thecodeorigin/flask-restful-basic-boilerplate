from functools import wraps

from ..constants.exceptions import ForbiddenException
from ...app.models.role import RoleModel

def role_guard(role_name_list: list, get_jwt_func):
  def decorator(f):
    @wraps(f)
    def check_role(*args, **kwargs):
      user_role_id = get_jwt_func()['sub']['role_id']
      user_role = RoleModel.find_by_id(user_role_id)

      if (user_role is None) or (user_role.name not in role_name_list):
        raise ForbiddenException
      
      return f(*args, **kwargs)
    return check_role
  return decorator
