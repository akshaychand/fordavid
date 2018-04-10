from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

mail = Mail()

migrate = Migrate()

db = SQLAlchemy()
