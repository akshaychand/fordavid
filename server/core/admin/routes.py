from flask_restplus import Namespace, Resource


# Admin
admin_api = Namespace('System Administration', description='Apis for managing system settings')

admin_model = admin_api.model('Admin', {
})


@admin_api.route('/', endpoint='admins')
class AdminApi(Resource):

    def get(self):
        return 'hello world!'


user_api = Namespace('Users Management', description='Apis for managing system users')

user_model = user_api.model('User', {

})


@user_api.route('/', endpoint='users')
class UsersApi(Resource):

    def get(self):
        return 'hello user'

    def post(self):
        return 'hello user'


@user_api.route('/<int:user_id>', endpoint='user')
class UserApi(Resource):

    def get(self, user_id):
        return user_id

    def put(self, user_id):
        return user_id

    def delete(self, user_id):
        return user_id


# Roles
role_api = Namespace('Roles Management', description='Apis for managing system roles')

role_model = role_api.model('Role', {

})


@role_api.route('/', endpoint='roles')
class RolesApi(Resource):

    def get(self):
        return 'hello role'

    def post(self):
        return 'hello role'


@role_api.route('/<int:role_id>', endpoint='role')
class RoleApi(Resource):

    def get(self, role_id):
        return role_id

    def put(self, role_id):
        return role_id

    def delete(self, role_id):
        return role_id
