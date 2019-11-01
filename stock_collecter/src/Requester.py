import json
import time
import requests
from Config import get_config
from Data_manager import save_multiple

query = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey={}&symbol={}&outputsize=full"

config = get_config()


def request_stock(ticker):
    key = config["REQUESTER"]["API_KEY_ALPHA_VANTAGE"]
    q = query.format(key, ticker)
    print("Fetching data ({}) ...".format(ticker))
    ans = requests.get(q)
    json_object = json.loads(ans.content.decode('utf-8'))
    days = json_object.get("Time Series (Daily)")
    if days is None:
        print(json_object)
        return None
    print(days)
    save_multiple([[ticker] + [d] + [t[1] for t in sorted(days.get(d).items(), key=lambda x: x[0])] for d in days])
    return "OK"


def request_all_stocks():
    delay = config["REQUESTER"]["SLEEP_BETWEEN_REQUESTS"]
    symbols = list(config["STOCKS"].keys())
    for s in symbols:
        try:
            request_stock(s)
        except Exception as e:
            print(e)
        time.sleep(delay)

