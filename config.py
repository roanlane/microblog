# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'rolanlane'
MAIL_PASSWORD = '19950303'

# administrator list
ADMINS = ['rolanlane@gmail.com']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}

MS_TRANSLATOR_CLIENT_SECRET = '90058c79524444e9b0679430d0b7d533'

SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5