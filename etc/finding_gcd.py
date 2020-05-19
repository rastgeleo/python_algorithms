def finding_gcd(a, b):
    """Euclid's algorithm
       21 = 1 * 12 + 9
       12 = 1 * 9 + 3
       9 = 0 * 3 + 0
    """
    while (b != 0):
        result = b
        a, b = b, a % b
        print(a, b)
    return result


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print('passed')


if __name__ == '__main__':
    test_finding_gcd()
