import logging
from datetime import datetime

from src.Datamanager import Datamanager
from src.Requester import Requester


class Portfolio:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.cash = None
        self.date = None
        self.holdings = {}
        self.r = Requester()

    def init(self, name):
        self.name = name

    def print(self):
        print("Name:\t", self.name)
        print("cash:\t", self.cash)
        print("date:\t", self.date)
        print("holdings:\t", self.holdings)

    def save(self):
        dm = Datamanager()
        dm.save_portfolio(self)

    def load(self, name, date):
        dm = Datamanager()
        p_data = dm.load_portfolio(name, date)
        if p_data:
            self.name = p_data['name']
            self.holdings = p_data['holdings']
            self.cash= p_data['cash']
            self.date= p_data['date']
            return True
        else:
            logging.warning("Can't load portfolio at - {} - {}".format(name, date))
            return False

    def strategy(self):
        logging.warning("No extention from base class!")

    def update(self):
        self.update_holdings()
        logging.info("cash".format(self.cash))
        self.strategy()
        self.save()

    def update_holdings(self):
        logging.info(self.holdings.keys())
        for symbol in self.holdings.keys():
            stock = self.r.get_stock_as_json(symbol, self.date)
            if 'error' not in stock.keys():
                self.holdings[symbol] = stock

    def buy(self, symbol, volume=None):
        stock = self.r.get_stock_as_json(symbol, self.date)
        try:
            if self.cash < stock['adjusted_close']:
                logging.info("Can't buy - not enough money, cash:{}, symbol:{}, value: {}".format(self.cash, symbol, stock['adjusted_close']))
                return False
            if symbol not in self.holdings.keys():
                self.holdings[symbol] = stock
                self.cash -= stock['adjusted_close']
                logging.info("Bought: {}, value: {}".format(symbol, stock['adjusted_close']))
            return True
        except Exception as e:
            logging.error(e)

    def sell(self, symbol=None):
        if symbol in self.holdings.keys():
            stock = self.holdings[symbol]
            logging.info("Date: {} - expected date set: {}".format(stock['date'], self.date))
            if stock['date'].strftime("%Y-%m-%d") != self.date:
                logging.error("Can't sell at this date {} - {} - {}".format(symbol, stock['date'], self.date))
                return False
            self.cash += stock['adjusted_close']
            self.holdings.pop(symbol)
            logging.info("Sold {} - for {} ".format(symbol, stock['adjusted_close']))

    def get_value(self):
        holdings_value = sum([stock['adjusted_close'] for stock in self.holdings.values()])
        return holdings_value + self.cash

    def get_holdings(self):
        return self.holdings.keys()

    def set_date(self, date=None):
        if date:
            self.date = date
        else:
            self.date = datetime.now().strftime("%Y-%m-%d")