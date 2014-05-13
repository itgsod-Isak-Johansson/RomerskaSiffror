#coding: latin-1
import random
from collections import OrderedDict


def romanize(number):
    """Funktionen tar ett nummer och returnerar rommerska siffror av det."""
    roman_numerals = OrderedDict([(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
    (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')])

    output = ''

    #om numret är negativt eller 0 skickar den ett ValueError
    if number == 0:
        raise(ValueError('can not romanize zero'))
    if number < 0:
        raise(ValueError('can not romanize negative numbers'))

    print number
    #Jag loopar igenom min dictionary, och får då en key och ett value som jag sedan använder för att få reda på hur
    #  många av X value jag ska lägga till i output.
    for key, value in roman_numerals.iteritems():
        output += value * (number/key)
    # resterna från divitionen number/key blir nya number.
        number = number % key

    print output
    return output



romanize(random.randint(1,10000))