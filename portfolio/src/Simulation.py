import logging
from datetime import datetime, timedelta

from src.domain.DefaultPortfolio import DefaultPortfolio
from src.domain.DummyPortfolio import DummyPortfolio


class Simulation:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.portfolio = None

    def run(self, start, stop):
        p_name = "test_portfolio31"
        p = DefaultPortfolio()
        # p = DummyPortfolio()

        p.init(p_name)
        p.cash = 1000
        p.set_date(start)
        p.save()
        p.print()
        logging.info(p.holdings.keys())
        for date in self._get_date_between(start, stop):
            yesterday = self._get_yesterday(date)
            p.load(p_name, yesterday)
            p.print()
            p.set_date(date)
            p.update()
            logging.info("Portfolio value: {}".format(p.get_value()))
            p.save()

    def _get_date_between(self, start, stop):
        startd = datetime.strptime(start, "%Y-%m-%d").date()
        stopd = datetime.strptime(stop, "%Y-%m-%d").date()
        delta = stopd - startd
        return [(startd + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

    def _get_yesterday(self, current_date):
        d = datetime.strptime(current_date, "%Y-%m-%d").date()
        return datetime.strftime(d - timedelta(1), '%Y-%m-%d')


s = Simulation()
s.logger.setLevel(logging.WARN)
s.run("2018-10-12", "2020-01-01")
# s.run("2019-03-01", "2020-01-01")