import mysql.connector
import pandas as pd

# DB = os.environ['STOCK_DB_PATH']
# print(DB)

mydb = mysql.connector.connect(host='mysql',
                               user='root',
                               password='test',
                               auth_plugin='mysql_native_password',
                               database='stocks'
                               )


def get(symbol):
    return pd.read_sql_query("SELECT * FROM stocks WHERE symbol = '{}';".format(symbol), mydb)


def get_distinct():
    return pd.read_sql_query("SELECT DISTINCT(symbol) FROM stocks;", mydb)


def query(q):
    return pd.read_sql_query(q, mydb)


def get_stock(symbol, limit=10):
    return query("SELECT * FROM stocks WHERE symbol = '{}' ORDER BY date DESC LIMIT {};".format(symbol, limit))


def get_stock_at_date(symbol, date, days_limit):
    return query(
        "SELECT * FROM stocks WHERE symbol = '{}' AND date <= '{}' ORDER BY date DESC LIMIT {};".format(symbol,
                                                                                                           date,
                                                                                                           days_limit))


def get_distinct_stocks():
    return query("SELECT DISTINCT symbol FROM stocks;")
