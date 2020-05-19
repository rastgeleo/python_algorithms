# 1 1 2 3 5 8 13 21 ...
def find_fibonacci_seq(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, b)
    return a


def test_find_fib():
    n = 10
    assert(find_fibonacci_seq(n) == 55)
    print('passed')


if __name__ == '__main__':
    test_find_fib()
