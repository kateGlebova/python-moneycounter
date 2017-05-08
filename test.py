import unittest
import operation
import datetime

class TestOperation(unittest.TestCase):

    def test_get_date(self):
        time = datetime.datetime.today()
        x = operation.Operation(time, "donate", 228)
        self.assertEquals(x.get_date(), time)

    def test_get_description(self):
        x = operation.Operation(datetime.datetime.today(), "donate", 228)
        self.assertEquals(x.get_description(), "donate")

    def test_get_money(self):
        x = operation.Operation(datetime.datetime.today(), "donate", 228)
        self.assertEquals(x.get_money(), 228)