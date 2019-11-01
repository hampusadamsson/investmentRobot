import json
import logging

import pymongo


class Datamanager:
    def __init__(self):
        self.logger = logging.getLogger()
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["portfolio"]
        self.cursor = mydb["p"]

    def save_portfolio(self, p):
        data = {
            '_id': p.name + p.date,
            'name': p.name,
            'holdings': p.holdings,
            'cash': p.cash,
            'date': p.date,
        }

        try:
            self.cursor.insert_one(data)
        except Exception as e:
            self.cursor.replace_one({'_id': data['_id']}, data, upsert=True)

    def load_portfolio(self, name, date):
        last = self.cursor.find_one({"name": name, "date": date})
        logging.info("Loading portfolio - name:{} - date:{} - returned:{}".format(name, date, str(last)))
        if last:
            return last
        return False
