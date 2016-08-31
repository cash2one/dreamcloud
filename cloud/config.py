# -*- coding: utf-8 -*-

import os

class DefaultConfig(object):

    PROJECT = "dreamcloud"

    DEBUG = False
    TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    # SECRET_KEY = 'your secret key'
    SECRET_KEY = "~!@@#@WERW"

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    # MYSQL for production.
    SQLALCHEMY_DATABASE_URI = 'mysql://vagrant:skydreamever@localhost/dreamvm?charset=utf8'



    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
