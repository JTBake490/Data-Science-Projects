from collections import namedtuple

Symbols = namedtuple('Symbols', 'thousand, nine_hundred, five_hundred, four_hundred, hundred, ninety, fifty, fourty, ten, nine, five, four, one')
numerals = Symbols('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
numbers = Symbols(1_000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)