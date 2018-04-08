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