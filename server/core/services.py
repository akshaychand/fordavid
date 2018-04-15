from .admin.services import UserService, RoleService
from .utils import SQLService, ModelService, CacheService

users = UserService()

roles = RoleService()

cache = CacheService()

