from flask_restplus import Namespace, Resource, fields

api = Namespace('System Administration', description='Apis for managing system settings', path='/admin')

admin = api.model('Admin', {

})


@api.route('/')
class AdminApi(Resource):

    def get(self):
        return 'hello world!'
