from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

mail = Mail()

migrate = Migrate()

db = SQLAlchemy()

api = Api(title='Loan Manager', version=1.0, description='API server for Consumer Loan Management')




