class Config(object):

    DEBUG = True

class ProductionConfig(Config):

    DEBUG = False

class DevelopmentConfig(Config):

    DEBUG = True

class TestingConfig(Config):

    DEBUG = True