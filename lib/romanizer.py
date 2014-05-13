import random
from collections import OrderedDict



def romanize(number):

    roman_numerals = OrderedDict([(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
    (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')])

    output = ''

    if number == 0:
        raise(ValueError('can not romanize zero'))
    if number < 0:
        raise(ValueError('can not romanize negative numbers'))
    print number

    for key, value in roman_numerals.iteritems():
        output += value * (number/key)
        number = number % key

    print output
    return output



romanize(random.randint(1,10000))