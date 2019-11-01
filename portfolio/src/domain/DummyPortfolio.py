import json
import logging
import operator
import random

import requests
from src.domain.Portfolio import Portfolio


class DummyPortfolio(Portfolio):
    def strategy(self):
        '''
        Strategy is called after the portfolio has been updated
        Use beneath functions to update your portfolio:
            self.buy(symbol)
            self.sell/symbol)
        :return:
        '''

        #Sell
        holds = self.get_holdings()
        amount = random.randint(0, max(0, len(holds)-1))
        selected = random.sample(holds, amount)
        for s in selected:
            self.sell(s)

        # Buy
        symbols = self.r.get_symbols()
        amount = random.randint(0, 5)
        selected = random.sample(symbols, amount)
        for s in selected:
            self.buy(s)

        logging.info("cash: {}".format(self.cash))