from flask_restplus import Api

from .admin.admin import api as admin_ns
from .admin.user import api as admin_user_ns
from .admin.role import api as admin_role_ns

from .loans.loan import api as loan_ns

from .postman.postman import api as postman_ns


api = Api(title='Loan Manager',
          version=1.0,
          description='API server for Consumer Loan Management')

# Admin namespace
api.add_namespace(admin_ns, path='/admin')
api.add_namespace(admin_user_ns, path='/admin/users')
api.add_namespace(admin_role_ns, path='/admin/roles')

# Loans namespace
api.add_namespace(loan_ns, path='/loans')

# Postman namespace
api.add_namespace(postman_ns, path='/docs/postman')


