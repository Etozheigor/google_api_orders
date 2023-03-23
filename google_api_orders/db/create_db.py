import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv


load_dotenv()

USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']


def create_db():
    """Создает базу данных orders_db в PostgreSQL"""
    try:
        connection = psycopg2.connect(user=USER, password=PASSWORD)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_database = cursor.execute('create database orders_db')
        cursor.close()
        connection.close()
    except Exception:
        print('Ошибка при создании базы данных')


if __name__ == '__main__':
    create_db()
