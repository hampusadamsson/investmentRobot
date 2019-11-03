import argparse

from Data_manager import get, get_distinct
from Requester import request_stock, request_all_stocks

if __name__ == '__main__':
    '''
        Python program to fetch and store stock data from Alpha vantage.
        e.g. 
                python Stock.py request -symbol MSFT
                python Stock.py requestall
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="action")
    parser.add_argument("-symbol", help="Ticker symbol to fetch")
    args = parser.parse_args()

    print(args.action)

    if args.action == "get":
        print(get(args.symbol))

    elif args.action == "request":
        request_stock(args.symbol)

    elif args.action == "requestall":
        request_all_stocks()

    elif args.action == "distinct":
        print(get_distinct())
