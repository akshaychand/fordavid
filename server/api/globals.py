from flask_restplus import Api
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


api = Api()

mail = Mail()

migrate = Migrate()

db = SQLAlchemy()
