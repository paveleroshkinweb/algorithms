import math


def placements(n, k):
    result = 1
    for i in range(0, k):
        result *= (n - i)
    return result


def placements_with_repetitions(n, k):
    return k ** n


def permutations(n):
    return math.factorial(n)


def permutations_with_repetitions(*args):
    n = math.factorial(sum(args))
    for k in args:
        n /= math.factorial(k)
    return n


def combinations(n, k):
    return placements(n, k) // math.factorial(k)


def combinations_with_repetitions(n, k):
    return combinations(n+k-1, k)


def subfactorial(n):
    result = permutations(n)
    for i in range(1, n+1):
        result += (-1) ** n * combinations(n, i) * permutations(n-i)
    return result


# 1 + 2 + .. + n
def sum1(n):
    return n*(n+1) / 2


# 1*2 + 2*3 + ... + n * (n+1)
def sum2(n):
    return n * (n+1) * (n+2) / 3


# 1*2*3 + 2*3*4 + ... + n*(n+1)*(n+2)
def sum3(n):
    return n * (n+1) * (n+2) * (n+3) / 4


# 1^2 + 2^2 + ... + n^2
def sum4(n):
    return n * (n+1) * (2*n+1) / 6


# 1^3 + 2^3 + ... + n^3
def sum5(n):
    return (n ** 2) * ((n+1) ** 2) / 4
