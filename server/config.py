class Config(object):

    DEBUG = True
    TEST = False

    # Mail
    MAIL_SERVER = ''
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = TEST
    MAIL_ASCII_ATTACHMENTS = False

    # SQL Databases
    SQLALCHEMY_DATABASE_URI = 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {
        'admin': 'postgresql://www-data:mysecretpassword@localhost:5432/admin',
        'loan_manager': 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    }
    SQLALCHEMY_ECHO=True


class ProductionConfig(Config):

    DEBUG = False
    TEST = False

    # Mail
    MAIL_SERVER = ''
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = TEST
    MAIL_ASCII_ATTACHMENTS = False

    # SQL Databases
    SQLALCHEMY_DATABASE_URI = 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {
        'admin': 'postgresql://www-data:mysecretpassword@localhost:5432/admin',
        'loan_manager': 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    }
    SQLALCHEMY_ECHO=False


class DevelopmentConfig(Config):

    DEBUG = True
    TEST = False

    # Mail
    MAIL_SERVER = ''
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = True
    MAIL_ASCII_ATTACHMENTS = False

    # SQL Databases
    SQLALCHEMY_DATABASE_URI = 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {
        'admin': 'postgresql://www-data:mysecretpassword@localhost:5432/admin',
        'loan_manager': 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    }


class TestingConfig(Config):

    DEBUG = True
    TEST = True

    # Mail
    MAIL_SERVER = ''
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = TEST
    MAIL_ASCII_ATTACHMENTS = False

    # SQL Databases
    SQLALCHEMY_DATABASE_URI = 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {
        'admin': 'postgresql://www-data:mysecretpassword@localhost:5432/admin',
        'loan_manager': 'postgresql://www-data:mysecretpassword@localhost:5432/loan_manager'
    }


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}