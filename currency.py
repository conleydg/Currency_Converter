
# Must be created with an amount and a currency code.

# Must equal another Currency object with the same amount and currency code.

# Must NOT equal another Currency object with different amount or currency code.


# Must be able to be added to another Currency object with the same currency code.

# Must be able to be subtracted by another Currency object with the same currency code.

# Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.


# Must be able to be multiplied by an int or float and return a Currency object.
# Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
class MyException(Exception):
    pass


class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code


    def __eq__(self, other):
        return self.amount == other.amount

    def __eq__(self, other):
        return self.currency_code == other.currency_code

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount + other.amount
        else:
            raise MYException

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount - other.amount
        else:
            raise MYException("something bad happened")

    def __mul__(self, other):
        try:
            return (self.currency_code, self.amount * float(other))
        except:
            raise MYException("something bad happened")




    # def is_currency_equal(self, other_currency_class):
    #     if self.currency_code == other_currency_class.currency_code:
    #         return True
    #
    # def add_currency(self, other_currency_class):
    #     if self.currency_code == other_currency_class.currency_code:
    #         print(self.amount + other_currency_class.amount)
    #     else:




    # def add_currency(self, other_amount, other_currency_code)
