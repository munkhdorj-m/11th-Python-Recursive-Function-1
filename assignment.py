def fibonacci(n):
    pass

def count_digits(n):
    for i in range(10):
        print(i)
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

def sum_digits(n):
    for i in range(10):
        print(i)
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
