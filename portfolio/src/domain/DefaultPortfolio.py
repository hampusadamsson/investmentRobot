import json
import logging
import operator
import requests
from domain.Portfolio import Portfolio


IP_predictor = "127.0.0.1"
PORT_predictor = 5002


class DefaultPortfolio(Portfolio):
    def strategy(self):
        '''
        Strategy is called after the portfolio has been updated
        Use beneath functions to update your portfolio:
            self.buy(symbol)
            self.sell/symbol)
        :return:
        '''

        # Get and predict all
        all_decisions = {}
        for symbol in self.r.get_symbols()[:15]:
            logging.info(self.date)
            stock = self.r.get_stock_as_json(symbol, self.date)
            logging.info(stock)
            if 'error' not in stock.keys():
                all_decisions[symbol] = self.predict_stock(symbol, self.date)[1]
                logging.info("Result: {}".format(str(all_decisions[symbol])))

        sorted_decision = sorted(all_decisions.items(), key=operator.itemgetter(1), reverse=True)

        #Sell
        for symbol, prob in sorted_decision:
            if prob < .5:
                self.sell(symbol)

        # Buy
        for symbol, prob in sorted_decision:
            if prob > .65:
                self.buy(symbol)

        logging.info("cash: {}".format(self.cash))

    @staticmethod
    def _predict_stock(df):
        url = "http://{}:{}/invocations".format(IP_predictor, PORT_predictor)
        headers = {
            'Content-Type': 'application/json; format=pandas-split',
        }

        response = None
        try:
            response = requests.post(url, headers=headers, data=df.to_json(orient='split'))
            latest_date_pred = json.loads(response.text)[-1]  # Return last (latest day from input) - [0, 1] = (0) sell, (1) buy.
            return latest_date_pred
        except Exception as e:
            logging.error("Error: {}, Message: {} \n Is the prediction service online?".format(str(e), response))
            return [0, 0]

    def predict_stock(self, ticker, date=None):
        logging.info("predicting: ".format(ticker))
        df = self.r.get_stock(ticker, date)
        return self._predict_stock(df)