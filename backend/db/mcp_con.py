# import pymysql
import psycopg2


def connection_db_mcp():
    # conn = pymysql.connect(
    #     host='127.0.0.1',
    #     database='db_chatbot',
    #     user="root",
    #     password="",
    #     autocommit=True,
    #     port=3306
    # )

    # --- Konfigurasi PostgreSQL ---
    pg_config = {
    'host': '188.166.224.240',
    'user': 'angga',
    'password': 'Elmecon2025',
    'dbname': 'openbravo',
    'port':5432
}

    # --- Koneksi ke PostgreSQL dan tarik data ---
    conn = psycopg2.connect(**pg_config)

    return conn