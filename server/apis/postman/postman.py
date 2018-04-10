from flask_restplus import Namespace, Resource, fields

api = Namespace('Postman documentation', description='Apis to simulate postman requests', path='/postman')

loans = api.model('Postman', {

})


@api.route('/')
class PostmanApi(Resource):

    def get(self):
        return api.as_postman(True, True)
