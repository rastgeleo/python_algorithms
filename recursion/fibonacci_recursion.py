def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)



def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a
