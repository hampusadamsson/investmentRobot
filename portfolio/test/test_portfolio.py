from unittest import TestCase

from src.Requester import Requester
from src.domain.Portfolio import Portfolio


class TestPortfolio(TestCase):
    def test_save_portfolio(self):
        p = Portfolio("test-1-dummy", "123")
        p.set_date("1970-01-01")
        p.cash = 124
        p.print()
        p.save()

    def test_load_portfolio(self):
        p = Portfolio("_", "_")
        p.load("test-1-dummy", "1970-01-01")
        p.print()

    def test_save_and_load_complex(self):
        p = Portfolio("test-1-dummy", "123")
        p.set_date("1970-01-01")
        p.cash = 1000
        stock = Requester().get_stock_as_json("MSFT", "2018-01-04")
        p.buy(stock)
        p.print()
        p.save()

        p2 = Portfolio("rnd", "")
        assert p2 != p
        assert p2.holdings == {}
        p2.load("test-1-dummy", "1970-01-01")
        p2.print()