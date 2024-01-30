def gramsToOunces(mass):
    return 28.3495231 * mass

def centigrade(f):
    return (5/9) - (f - 32)

def solve(numheads, numlegs):
    rabits, chickens = numheads, 0
    while rabits*4 + chickens*2 != numlegs:
        rabits -= 1
        chickens += 1
    return [rabits, chickens]

def filter_primes(nums):
    primes = []
    for n in nums:
        p = True
        for i in range(2, n**0.5):
            if n%i == 0:
                p = False
        if p:
            primes.append(n)
    return primes

def perm(s, ind=0):
    if ind == len(s) - 1:
        print(s)
        return

    for i in range(ind, len(s)):
        s_list = list(s)
        s_list[ind], s_list[i] = s_list[i], s_list[ind]
        new_string = ''.join(s_list)

        perm(new_string, ind + 1)

        s_list[ind], s_list[i] = s_list[i], s_list[ind]

def reversedSentence(user_string):
    return ' '.join(reversed(user_string.split()))

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True
    return False

def spy_game(nums):
    spy = [0, 0, 7]
    ind = 0 
    for i in range(len(nums)):
        if spy[ind] == nums[i]:
            ind += 1
    return ind == 3

def volumeOfSphere(r):
    return (4/3) * 3,14 * r**3

def uniqueList(n):
    values = dict()
    for i in n:
        values[i] = 0
    r = []
    for i in values.keys():
        r.append(i)
    return r

def palindrome(s):
    return s == ''.join(reversed(list(s)))

def histogram(nums):
    for i in nums:
        print('*'*i)
    
from random import randint

def guessTheNumber():
    print('Hello! What is your name?')
    name = input()
    count = 0
    number = randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    temp = 0
    while temp != number:
        print('Take a guess.')
        temp = int(input())
        if temp < number:
            print('\nYour guess is too low.')
        elif temp > number:
            print('\nYour guess is too high.')
        count += 1

    print(f'Good job, {name}! You guessed my number in {count} guesses!')

