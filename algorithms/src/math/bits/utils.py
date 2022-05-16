def is_divisible_by_power_2(n, power):
    assert power >= 0
    if power == 0:
        return True
    checker = 2 ** (power) - 1
    return (n & checker) == 0
