import psycopg2
from sqlalchemy import create_engine
from decouple import config
import logging


def check_connection():

    connection = None

    try:

        connection = psycopg2.connect(
            host=config('DB_HOST'), database=config('DB_NAME'), user=config('DB_USER'), password=config('DB_PASS'))

        cursor = connection.cursor()
        cursor.execute("SELECT datname FROM pg_database;")
        databases = cursor.fetchall()
        assert (((config('DB_NAME'),) in databases) == True)
        logging.info(f'Database found: "{config("DB_NAME")}"')

    except:
        logging.error('Database not connected')

    connection.close()


def connect_2db():

    try:
        DATABASE_URI = f'postgresql+psycopg2://{config("DB_USER")}:{config("DB_PASS")}@{config("DB_HOST")}:{config("DB_PORT")}/{config("DB_NAME")}'
        db = create_engine(DATABASE_URI)
        conn = db.connect()
        return conn
    except:
        logging.error('Could not connect to Database')
