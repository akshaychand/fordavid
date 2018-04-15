from server.core.utils.data import ModelService
from .models import User, Role


class UserService(ModelService):

    def __init__(self):
        super(UserService, self).__init__()
        self.__model__ = User
        self.__bind_key__ = 'admin'


class RoleService(ModelService):

    def __init__(self):
        super(RoleService, self).__init__()
        self.__model__ = Role
        self.__bind_key__ = 'admin'

