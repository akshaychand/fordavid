from flask_restplus import Namespace, Resource, fields

api = Namespace('Role management', description='Apis for managing system roles', path='/role')

admin = api.model('Role', {

})


@api.route('/')
class RolesApi(Resource):

    def get(self):
        return 'hello role'

    def post(self):
        return 'hello role'


@api.route('/<int:role_id>')
class RoleApi(Resource):

    def get(self, role_id):
        return role_id

    def put(self, role_id):
        return role_id

    def delete(self, role_id):
        return role_id
