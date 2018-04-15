from flask_restplus import Namespace, Resource


# Loans
loans_api = Namespace('Loans Management', description='Apis for managing consumer loans')

loans_model = loans_api.model('Loans', {
})


@loans_api.route('/', endpoint='loans')
class AdminApi(Resource):

    def get(self):
        return 'hello world!'

    def post(self):
        return 'hello world!'


@loans_api.route('/<int:loan_id>', endpoint='loan')
class UsersApi(Resource):

    def get(self, loan_id):
        return 'hello user'

    def put(self, loan_id):
        return 'hello user'

    def delete(self, loan_id):
        return 'hello_user'
