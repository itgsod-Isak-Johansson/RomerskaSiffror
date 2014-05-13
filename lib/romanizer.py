import random
def romanize(number):
    output = ''
    if number == 0:
        raise(ValueError('can not romanize zero'))
    if number < 0:
        raise(ValueError('can not romanize negative numbers'))
    print number
    while number > 0:
        if number >= 1000:
            output += 'M'
            number = number - 1000
        elif number >=900:
            output += 'CM'
            number = number - 900
        elif number >=500:
            output += 'D'
            number = number - 500
        elif number >=400:
            output += 'CD'
            number = number - 400
        elif number >=100:
            output += 'C'
            number = number - 100
        elif number >=90:
            output += 'XC'
            number = number - 90
        elif number >= 50:
            output += 'L'
            number = number - 50
        elif number >= 40:
            output += 'XL'
            number = number - 40
        elif number >= 10:
            output += 'X'
            number = number - 10
        elif number >= 9:
            output += 'IX'
            number = number - 9
        elif number >= 8:
            output += 'VIII'
            number = number - 8
        elif number >= 7:
            output += 'VII'
            number = number - 7
        elif number >= 6:
            output += 'VI'
            number = number - 6
        elif number >= 5:
            output += 'V'
            number = number - 5
        elif number >= 4:
            output += 'IV'
            number = number - 4
        elif number >= 3:
            output += 'III'
            number = number - 3
        elif number >= 2:
            output += 'II'
            number = number - 2
        elif number >= 1:
            output += 'I'
            number = number - 1
    print output
    return output



romanize(random.randint(1,1000))