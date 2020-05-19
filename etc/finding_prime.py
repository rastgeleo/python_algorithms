import math
import random


def finding_prime(number):
    num = abs(number)
    if num < 4:  # 4보다 작은 수는 소수
        return True
    # Brute-force: num보다 작은 수중 나누어 떨어지는 수가 있으면 합성수
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number-1)
            if pow(a, number-1, number):
                return False
        return True


def test_finding_prime():
    number1 = 17  #331 fails on finding_prime_sqrt
    number2 = 121
    assert(finding_prime(number1) is True)
    assert(finding_prime(number2) is False)
    assert(finding_prime_sqrt(number1) is True)
    assert(finding_prime_sqrt(number2) is False)
    assert(finding_prime_fermat(number1) is True)
    assert(finding_prime_fermat(number2) is False)
    print('passed!')


if __name__ == '__main__':
    test_finding_prime()
