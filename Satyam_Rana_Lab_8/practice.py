# class CurrencyConverter:
#     def __init__(self):
#         self._exchnage_rate = 0.0
#     def set_exchange_rate(self, rate):
#         self._exchnage_rate = rate
#     def convert_to_currency(self, amount):
#         converted_currency = amount * self._exchnage_rate
#         return converted_currency
# def main():
#     cc = CurrencyConverter()
#     cc.set_exchange_rate(2.5)
#     val = cc.convert_to_currency(4)
#     print("Converted amount: ", val)

# main()

# class Person(object):
#     name = None
#     def __init__(self, name):
#         Person.name = name
#     def greet(self):
#         return "Hello, my name is " + self.name

# Circle all appropriate criticisms of this implementation.
# (A) Every Person’s name will be the equal to the most recently created Person’s name.


# def __init__(self, temp, units):
#     self.T = temp
#     self.units = units
# def TtoC(self):
#     if self.units == 'degF':
#         return (self.T-32)/1.8
#     elif self.units == 'degC':
#         return self.T
#     elif self.units == 'K':
#         return self.T - 273.15