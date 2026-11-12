import os
import pymysql
from pymysql.cursors import DictCursor


def abrir_conexao():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "passaporte_sulamericano"),
        charset="utf8mb4",
        cursorclass=DictCursor,
        connect_timeout=5,
    )
