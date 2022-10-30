import psycopg2
from decouple import config

connection = psycopg2.connect(
    host=config('DB_HOST'), database=config('DB_NAME'), user=config('DB_USER'), password=config('DB_PASS'))

cursor = connection.cursor()
cursor.execute(open("tables.sql", "r").read())

connection.commit()
connection.close()
