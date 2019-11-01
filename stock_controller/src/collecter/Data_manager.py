import sqlite3

import os
import pandas as pd

DB = os.environ['STOCK_DB_PATH']
print(DB)


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
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query("SELECT DISTINCT(symbol) FROM stocks;", conn)


def query(q):
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query(q, conn)


def get_stock(symbol, limit=10):
    return query("SELECT * FROM stocks WHERE symbol == '{}' ORDER BY date DESC LIMIT '{}';".format(symbol, limit))


def get_stock_at_date(symbol, date, days_limit):
    return query("SELECT * FROM stocks WHERE symbol == '{}' AND date <= '{}' ORDER BY date DESC LIMIT '{}';".format(symbol, date, days_limit))


def get_distinct_stocks():
    return query("SELECT DISTINCT symbol FROM stocks;")

