import sys
import math
from functools import reduce

def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

# if len(sys.argv) == 2:
#     print(is_prime(int(sys.argv[1])))

# maybe make a set of all of the numbers up to n,
# then remove the ones that you know aren't primes,
# like even numbers above 2, then numbers divisble
# by 3, 5, 7...

def sieve(n):
    """This doesn't work like The Sieve of Eratosthenes but I think it's pretty good. nvm not very good"""
    nums = [x for x in range(2, n + 1)]
    i = 0
    while i < len(nums)/nums[i]:
        nums = [n for n in nums if n == nums[i] or n % nums[i] != 0]
        i = i + 1
    return nums

# print(sieve(100))

def sieve_of_eratosthenes(n):
    """An implementation of The Sieve of Eratosthenes"""
    A = [True for x in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i] == True:
            y = [j for j in range(i*i, n + 1, i) if j < len(A)]
            for j in y:
                A[j] = False
    primes = [i for i in range(2, len(A)) if A[i] == True]
    return primes

# print(sieve_of_eratosthenes(100))
# print(sieve_of_eratosthenes(73))
primes = sieve_of_eratosthenes(2000000)
sum = reduce(lambda a, b: a + b, primes)
# print(sum)
print(sum == 142913828922) # checking the sum of primes up to 2 million

if len(sys.argv) == 2:
    print(sieve_of_eratosthenes(int(sys.argv[1])))
# def primes_from_sets(n):
#     primes = {x for x in range(2, n + 1)}
#     for p in primes:
#         primes = primes - {p*p + n*p for n in range(0, int(n + 1 / p))}
#     return primes

# def primes_from_sets(n):
#     primes = {x for x in range(2, n + 1)}
#     for p in primes:
#         primes = primes - {n for n in range(p*p, n + 1, p)}
#     return primes
