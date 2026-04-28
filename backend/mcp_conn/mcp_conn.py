# import pymysql
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('../../.env')



def connection_db_mcp():
    # conn = pymysql.connect(
    #     host='127.0.0.1',
    #     database='db_chatbot',
    #     user="root",
    #     password="",
    #     autocommit=True,
    #     port=3306
    # )

    pg_config = {
    'host': os.environ.get('HOST_OB'),
    'user': os.environ.get('USER_OB'),
    'password': os.environ.get('PASS_OB'),
    'dbname': os.environ.get('DB_OB'),
    'port':os.environ.get('PORT_OB')
}

    # --- Koneksi ke PostgreSQL dan tarik data ---
    conn = psycopg2.connect(**pg_config)

    return conn