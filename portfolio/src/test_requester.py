from unittest import TestCase

from Requester import Requester


class TestRequester(TestCase):
    def test_get_stock(self):
        r = Requester()
        print(r.get_stock("INX"))
