from collections import defaultdict
from functools import lru_cache
from math import prod


def form(dividers):
    if len(dividers) == 1:
        number = next(iter(dividers.keys()))
        power = dividers[number]
        return f'{number} {number ** 2} {number ** (power - 3)}'
    if len(dividers) == 2:
        numbers = list(dividers.keys())
        res = [numbers[0], numbers[1], numbers[0] ** (dividers[numbers[0]] - 1) * numbers[1] ** (dividers[numbers[1]] - 1)]
        return ' '.join([str(n) for n in res])
    if len(dividers) == 3:
        return ' '.join([str(n ** dividers[n]) for n in dividers])
    new_dividers = [n ** dividers[n] for n in dividers]
    diff = len(new_dividers) - 3
    res = [prod(new_dividers[:diff+1])] + new_dividers[diff+1:]
    return ' '.join([str(n) for n in res])


def count_power(power):
    if power <= 2:
        return 1
    if 3 <= power <= 5:
        return 2
    return 3


def check_dividers(dividers):
    if len(dividers) >= 3:
        return True
    powers = list(dividers.values())
    if len(dividers) == 2 and powers[0] + powers[1] >= 4:
        return True
    count = 0
    for power in powers:
        count += count_power(power)
        if count >= 3:
            return True
    return False


def merge_dividers(dividers1, dividers2):
    merged_dividers = {**dividers1}
    for key in dividers2:
        if key in merged_dividers:
            merged_dividers[key] += dividers2[key]
        else:
            merged_dividers[key] = dividers2[key]
    return merged_dividers


@lru_cache(10 ** 9)
def partial_dividers(n):
    i = 2
    dividers = defaultdict(lambda: 0)
    while i * i <= n:
        if n % i == 0:
            dividers[i] += 1
            if check_dividers(dividers):
                return True, dividers
            is_dividable_child, child_dividers = partial_dividers(n // i)
            dividers = merge_dividers(dividers, child_dividers)
            if is_dividable_child or check_dividers(dividers):
                return True, dividers
            return False, dividers
        else:
            i += 1
    dividers[n] += 1
    return False, dividers


def find_dividers(n):
    is_dividable, dividers = partial_dividers(n)
    if is_dividable:
        return f"YES\n{form(dividers)}"
    return "NO"


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        res = find_dividers(int(input()))
        results.append(res)
    print("\n".join(results))
