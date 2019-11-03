import mysql.connector
import pandas as pd

from Config import get_config

mydb = mysql.connector.connect(host='0.0.0.0', #mysql
                               user='root',
                               password='test',
                               auth_plugin='mysql_native_password',
                               database='stocks'
                               )


def save_multiple(queries):
    c = mydb.cursor()
    for q in queries:
        c.execute("INSERT IGNORE INTO stocks VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                  .format(q[0]+q[1], *q))
    mydb.commit()


def get(symbol):
    return pd.read_sql_query("SELECT * FROM stocks WHERE symbol = '{}';".format(symbol), mydb)


def get_distinct():
    return pd.read_sql_query("SELECT DISTINCT(symbol) FROM stocks;", mydb)
