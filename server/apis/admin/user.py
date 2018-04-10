from flask_restplus import Namespace, Resource, fields

api = Namespace('User management', description='Apis for managing system users', path='/user')

admin = api.model('User', {

})


@api.route('/')
class UsersApi(Resource):

    def get(self):
        return 'hello user'

    def post(self):
        return 'hello user'


@api.route('/<int:user_id>')
class UserApi(Resource):

    def get(self, user_id):
        return user_id

    def put(self, user_id):
        return user_id

    def delete(self, user_id):
        return user_id
