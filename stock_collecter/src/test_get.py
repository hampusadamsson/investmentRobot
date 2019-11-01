from unittest import TestCase

from Data_manager import get, get_distinct


class TestGet(TestCase):
    def test_get(self):
        res = get("MSFT")
        assert res is not None

    def test_get_distinct(self):
        res = get_distinct()
        assert res is not None
