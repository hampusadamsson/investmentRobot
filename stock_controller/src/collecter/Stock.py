import argparse

from collecter.Data_manager import init_db, get, get_distinct
from collecter.Requester import request_stock, request_all_stocks

if __name__ == '__main__':
    '''
    e.g.    python Stock.py init
            python stock.py request -symbol MSFT 
            python Stock.py get -symbol MSFT
            
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="action")
    parser.add_argument("-username", help="Username for email")
    parser.add_argument("-symbol", help="Ticker symbol to fetch")
    parser.add_argument("-key", help="Alpha vantage API key")
    args = parser.parse_args()

    print(args.action)
    if args.action == "init":
        init_db()
    elif args.action == "get":
        print(get(args.symbol))
    elif args.action == "request":
        request_stock(args.key, args.symbol)
    elif args.action == "requestall":
        request_all_stocks(args.key)
    elif args.action == "distinct":
        print(get_distinct())
