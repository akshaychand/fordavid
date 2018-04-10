from flask_restplus import Api

from .admin import api as admin_ns

api = Api(title='Loan Manager', version=1.0, description='API server for Consumer Loan Management')

api.add_namespace(admin_ns, path="/admin")
