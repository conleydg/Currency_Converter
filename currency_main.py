from currency import *
from currency_converter import *



test_currency = Currency(5000, 'JPY')
test_currency_two = Currency(5000, 'JPY')
test_currency_three = Currency(5000, 'USD')

print('test_currency: ',test_currency.amount, test_currency.currency_code)
print('test_currency_two : ',test_currency_two.amount, test_currency_two.currency_code)
print('test_currency_three : ',test_currency_three.amount, test_currency_three.currency_code)

conversion_rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}

converter_one = CurrencyConverter(conversion_rates)

print('test_currency == test_currency_two: ', test_currency == test_currency_two)
print('test_currency != test_currency_three: ', test_currency != test_currency_three)

print('test_currency + test_currency_two: ', test_currency + test_currency_two)

print('test_currency - test_currency_two: ',test_currency - test_currency_two)
#
print('test_currency * 3', test_currency * 3)

#
converter_one.convert(test_currency, 'USD')

print('test_currency converted from JPY to USD: )
print(test_currency.amount, test_currency.currency_code)
#


# test_currency.add_currency(test_currency_two)
