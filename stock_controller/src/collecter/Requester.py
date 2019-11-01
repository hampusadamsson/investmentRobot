import requests
import json
import time
from pathlib import Path

from collecter.Data_manager import save_multiple

SP500 = str(Path(__file__).parent.parent) + "/resources/s&p500.txt"


query = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey={}&symbol={}&outputsize=full"


def request_stock(key, ticker):
    q = query.format(key, ticker)
    print("Fetching data ({}) ...".format(ticker))
    ans = requests.get(q)
    json_object = json.loads(ans.content.decode('utf-8'))
    days = json_object.get("Time Series (Daily)")
    if days is None:
        print(json_object)
        return None
    save_multiple([[ticker] + [d] + [t[1] for t in sorted(days.get(d).items(), key=lambda x: x[0])] for d in days])


def request_all_stocks(key, delay=15):
    with open(SP500, "r") as fn:
        symbols = fn.readlines()
    for s in symbols:
        request_stock(key, s.strip('\n'))
        time.sleep(delay)

