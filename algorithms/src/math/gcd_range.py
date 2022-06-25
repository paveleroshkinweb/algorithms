# Task: Count the numbers from i = [1, ..., r] with gcd(i, n) == 1

from itertools import combinations
from math import prod


def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


def primes(n):
    dividers = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            dividers.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        dividers.append(n)
    return dividers


# Time complexity: O(nlogn)
def gcd_range1(n, r):
    return len([
        number
        for number in range(1, r+1)
        if gcd(number, n) == 1
    ])


# Time complexity: O(n), most likely that it's O(sqrt(n))
def gcd_range2(n, r):
    dividers = primes(n)
    sign = 1
    count = 0
    for i in range(1, len(dividers) + 1):
        for c in combinations(dividers, i):
            count += sign * (r // prod(c))
        sign *= -1
    return r - count
