import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'aitest.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
