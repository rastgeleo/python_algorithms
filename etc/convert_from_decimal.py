def convert_from_decimal(number, base):
    result = 0
    multiplier = 1
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    return result


def convert_from_decimal_larger_bases(number, base):
    strings = '0123456789ABCDEFGHIJ'
    result = ''
    while number > 0:
        result = strings[number % base] + result
        number = number // base
    return result


def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)


def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == '1F')


if __name__ == '__main__':
    test_convert_from_decimal()
    test_convert_from_decimal_larger_bases()
