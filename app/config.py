import os

from databases import Database


DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
TESTING = os.environ.get('TEST')
DB_NAME = 'films_test' if os.environ.get('TEST') else os.environ.get('POSTGRES_DB')
SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
)
database = Database(SQLALCHEMY_DATABASE_URL)
