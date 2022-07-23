def is_divisible_by_power_2(n, power):
    assert power >= 0
    if power == 0:
        return True
    checker = (1 << power) - 1
    return (n & checker) == 0


def set_last_0(n):
    return n & (n-1)


def set_last_1(n):
    return n | (n+1)


def remove_trailing_1(n):
    return n & (n+1)


def remove_trailing_0(n):
    return n | (n-1)


def set_bit(n, position):
    return n | (1 << position)


def clear_bit(n, position):
    return n & ~(1 << position)


def read_bit(n, position):
    return n & (1 << position) >> position

