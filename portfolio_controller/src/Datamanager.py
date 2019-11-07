import json
import logging

import pymongo
from bson import json_util


class Datamanager:
    def __init__(self):
        self.logger = logging.getLogger()
        # myclient = pymongo.MongoClient("mongodb://mongodb:27017/")
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["portfolio"]
        self.cursor = mydb["p"]

    def find(self):
        last = self.cursor.find_one({})
        return last

    def get_portfolio_names(self):
        portfolio_names = self.cursor.distinct("name")
        logging.info("Loading all portfolio names")
        return json.dumps(portfolio_names)

    def get_portfolio(self, portfolio_name):
        portfolio = self.cursor.find({"name": portfolio_name})
        logging.info("Loading portfolio - name:{}".format(portfolio_name))
        json_list = [json.dumps(day, default=json_util.default) for day in portfolio]
        return json.dumps(json_list)

    def load_portfolio_at_date(self, name, date):
        last = self.cursor.find_one({"name": name, "date": date})
        logging.info("Loading portfolio - name:{} - date:{} - returned:{}".format(name, date, str(last)))
        return last