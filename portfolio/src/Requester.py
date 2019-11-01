import logging
import pandas as pd
import requests


class Requester:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.IP = "127.0.0.1"
        self.PORT = 5001

    def get_health_check(self):
        logging.info("Health check...")
        url = "http://{}:{}/health".format(self.IP, self.PORT)
        response = requests.get(url)
        return response.text

    def get_symbols(self) -> list:
        url = "http://{}:{}/getDistinct".format(self.IP, self.PORT)
        response = requests.get(url)
        df = pd.read_json(response.text)
        return df.symbol.values.tolist()

    def get_stock(self, ticker, date=None, n_to_request=25):
        logging.info("Get stock: {},\t{}\t{}".format(ticker, date, n_to_request))
        if date:
            url = "http://{}:{}/getStockAtDate/{}/{}/{}".format(self.IP, self.PORT, ticker, date, n_to_request)
        else:
            url = "http://{}:{}/getStock/{}/{}".format(self.IP, self.PORT, ticker, n_to_request)
        response = requests.get(url)
        df = pd.read_json(response.text)
        return df.sort_values(by='date')

    def get_stock_as_json(self, ticker, date):
        try:
            ret = self.get_stock(ticker, date)
            json_stock = ret.to_dict(orient='index')[0]
            if json_stock["date"].strftime("%Y-%m-%d") == date:
                return json_stock
            else:
                logging.error("Date missmatch: expected:{} returned:{}".format(date, json_stock["date"]))
                return dict({'date': date,
                             'nearest date': json_stock['date'],
                             'error': 'invalid-date'})
        except Exception as e:
            logging.error(e)
            return dict({'error': e})

'''
    def _predict_stock(self, df):
        url = "http://{}:{}/invocations".format(self.IP_predictor, self.PORT_predictor)
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
        df = self.get_stock(ticker, date)
        return self._predict_stock(df)
'''