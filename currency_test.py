import unittest

from currency import *

class TestCurrency(unittest.TestCase):
    test_currency = Currency(5000, 'JPY')
    test_currency_two = Currency(5000, 'JPY')

    print(test_currency.amount)


    def Test_is_equal(self):
        self.assertEqual(test_currency,test_currency_two)





















if __name__ == '__main__':
    unittest.main()
