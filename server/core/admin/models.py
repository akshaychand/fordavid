from werkzeug.security import generate_password_hash, check_password_hash

from server.core.globals import db

role_user = db.Table('role_user',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                     info={'bind_key': 'admin'}
                     )


class User(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)

    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)

    roles = db.relationship('Role', secondary=role_user, backref=db.backref('users', lazy='dynamic'))

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def full_name(self):
        return (self.first_name or '') + ' ' + (self.last_name or '')

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def __str__(self):
        return '<User: {}>'.format(self.username)


class Role(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(100), nullable=False, unique=True)
    role_description = db.Column(db.String(255), nullable=False)

    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.role_name)

    def __str__(self):
        return '<Role: {}>'.format(self.role_name)
