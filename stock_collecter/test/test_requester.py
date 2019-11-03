from unittest import TestCase

from Config import get_config
from Requester import request_stock


class TestRequester(TestCase):

    def test_request(self):
        assert request_stock("AMZN") is not None

    def test_config(self):
        config = get_config()
        stocks = list(config["STOCKS"].keys())
        assert stocks[2] is not None
