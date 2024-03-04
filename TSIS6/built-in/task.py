from functools import reduce
import time
import math


def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

def is_palindrome(string):
    # return string == ''.join(reversed(string.split('')))
    return string == string[::-1]

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

def all_elements_true(tup):
    return all(tup)