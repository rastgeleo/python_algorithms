from math import log10, ceil


def karatsuba(x, y):
    """
    Karatsuba algorithm: A quicker algorithm for mutiplication of big numbers
    x and y is n digit, m < n. usually m = n/2
    x = a * 10^m + b
    y = c * 10^m + d
    xy = (a * 10^m + b)(c * 10^m + d)
       = z2 * 10^2m + z1 * 10^m + z0
       where, z2 = a * c
              z1 = (a + b)(c + d) - ac -bd
              z0 = b * d
    """
    # THe base case
    if x < 10 or y < 10:
        return x*y

    # set n to the number of digits in the highest
    n = max(int(log10(x)+1), int(log10(y)+1))

    # rounds up n/2
    n_2 = int(ceil(n/2.0))

    # splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd

    # performs the multiplication
    return (((10**(2*n_2))*ac) + bd + ((10**n_2)*(ad_bc)))
