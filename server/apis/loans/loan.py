from flask_restplus import Namespace, Resource, fields

api = Namespace('Loan Management', description='Apis for loan data management', path='/loans')

loans = api.model('Loan', {

})


@api.route('/')
class LoansApi(Resource):

    def get(self):
        return 'hello world!'

    def post(self):
        return 'Hello loan'


@api.route('/<int:loan_id>')
class LoanApi(Resource):

    def get(self, loan_id):
        return loan_id

    def put(self, loan_id):
        return loan_id

    def delete(self, loan_id):
        return loan_id