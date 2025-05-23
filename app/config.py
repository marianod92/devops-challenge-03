import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:root@db/db'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    #Database URL
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:root@db/db'

class ProductionConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@mysql/db'
