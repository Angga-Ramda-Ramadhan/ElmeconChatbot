from flask import current_app, g
import pymysql


def connection_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host='127.0.0.1',
            database='db_chatbot',
            user="root",
            password="",
            autocommit=True,
            port=3306
        )

    return g.db


def close_db_conn(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()