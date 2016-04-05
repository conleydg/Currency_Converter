

# Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
import sys

class DifferentCurrencyCodeError(Exception):
    pass


class Currency:
    def __init__(self, amount, currency_code):
            self.amount = amount
            self.currency_code = currency_code

    def __str__(self):
        return str(self.amount) + ('') + (self.currency_code)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def __ne__(self, other):
        return self.currency_code != other.currency_code or self.amount != other.amount

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency((self.amount + other.amount), self.currency_code)
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency((self.amount - other.amount), self.currency_code)
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, other):
        self.amount = self.amount * float(other)
        return self.amount, self.currency_code
