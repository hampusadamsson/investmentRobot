import sqlite3
import pandas as pd

from Config import get_config

DB = get_config()['DATABASE']["DATABASE_PATH"]


def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE stocks (
                     id TEXT PRIMARY KEY , 
                     symbol CHARACTER(6), 
                     date DATE, 
                     open REAL,
                     high REAL, 
                     low REAL, 
                     close REAL, 
                     adjusted_close REAL,
                     volume BIGINT,
                     dividend_amount REAL,
                     split_coefficient REAL)''')
        conn.commit()


def save_multiple(queries):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        for q in queries:
            c.execute("INSERT OR IGNORE INTO stocks VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(q[0]+q[1], *q))
        conn.commit()


def get(symbol):
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query("SELECT * FROM stocks WHERE symbol == '{}';".format(symbol), conn)


def get_distinct():
    print(DB)
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query("SELECT DISTINCT(symbol) FROM stocks;", conn)
