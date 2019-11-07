from unittest import TestCase

from src.Datamanager import Datamanager


class TestDatamanager(TestCase):
    def test_get_portfolios(self):
        dm = Datamanager()
        res = dm.get_portfolio_names()
        print(res)