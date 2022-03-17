from collections import defaultdict
from itertools import combinations
from math import prod


def find_factors(x):
    factors = defaultdict(lambda: 0)
    i = 2
    while i * i <= x:
        if x % i == 0:
            factors[i] += 1
            x //= i
        else:
            i += 1
    if x > 1:
        factors[x] += 1
    return factors


def find_optimal(x, factors):
    values = [key ** factors[key] for key in factors]
    if len(values) == 2:
        return f'{values[0]} {values[1]}'
    optimal = None
    for size in range(1, len(values) - 1):
        for subgroup in combinations(values, size):
            product = prod(subgroup)
            rest = x // product
            if not optimal or max(product, rest) < max(optimal):
                optimal = (product, rest)
    return f'{optimal[0]} {optimal[1]}'


def fadi_lcm(x):
    if x == 1:
        return '1 1'
    factors = find_factors(x)
    if len(factors) == 1:
        return '1 ' + str(x)
    return find_optimal(x, factors)


if __name__ == '__main__':
    x = int(input())
    print(fadi_lcm(x))