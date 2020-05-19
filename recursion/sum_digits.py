def sum_digits(n):
    if n < 10:
        return n
    last_digit = n % 10
    n = n // 10
    return last_digit + sum_digits(n)


def sum_digits_loop(n):
    
    result = 0
    while n > 0:
        digit = n % 10
        n = n // 10 
        result += digit
    return result


print(sum_digits(1234))
print(sum_digits_loop(1234))
