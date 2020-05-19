def convert_to_decimal(number, base):
    multiplier = 1
    result = 0
    while number > 0:
        # 첫자리수는 1을 곱하고 두번째 자리부터는 2^n을 곱해서 더한다
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result


def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)


if __name__ == '__main__':
    test_convert_to_decimal()
