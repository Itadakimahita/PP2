import math

class First:
    def getString(self):
        self.temp = input()
    def printString(self):
        print(self.temp)

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print([self.x, self.y])
    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y
    def dist(self, x, y):
        return math.sqrt(pow(y-self.y,2) + pow(x-self.x, 2))
    
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print(f'{self.owner} your balance: {self.balance}$')

    def withdraw(self, value):
        if self.balance < value:
            print(f'{self.owner} your balance: {self.balance}$')
        else:
            self.balance -= value
            print(f'{self.owner} your balance: {self.balance}$')

class PrimeNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        # for num in numbers:
        #     if num < 2:
        #         self.numbers.append(num)
        #     else:
        #         temp = True
        #         for i in range(2, int(num**0.5) + 1):
        #             if num % i == 0:
        #                 temp = False
        #         if temp:
        #             self.numbers.append(num)

    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.isPrime(x), self.numbers))
    
