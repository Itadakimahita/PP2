def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

def countdown(n):
    while n >= 0:
        yield n
        n -= 1
        