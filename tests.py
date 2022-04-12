import unittest
from converter import milli_centi, milli_deci, milli_kilo


class TestConv(unittest.TestCase):

    def test_milli_centi(self):
        self.assertTrue(milli_centi(10) == 1)
        self.assertTrue(milli_centi(0) == 0)
        self.assertTrue(milli_centi(542353425342) == 54235342534.2)

    def test_milli_deci(self):
        self.assertTrue(milli_deci(10) == 0.1)
        self.assertTrue(milli_deci(0) == 0)
        self.assertTrue(milli_deci(542353425342) == 5423534253.42)

    def test_milli_kilo(self):
        self.assertTrue(milli_kilo(10) == 1e-05)
        self.assertTrue(milli_kilo(0) == 0)
        self.assertTrue(milli_kilo(542353425342) == 542353.425342)

