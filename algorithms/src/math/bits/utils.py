def is_divisible_by_power_2(n, power):
    assert power >= 0
    if power == 0:
        return True
    checker = (1 << power) - 1
    return (n & checker) == 0


def set_bit_1(n, position):
    return n | 2 ** position


def clear_bit_1(n, position):
    return n & ~(2 ** (position))


def read_bit_1(n, position):
    return n & (2 ** position) >> position


def set_bit_2(n, position):
    return n | (1 << position)


def clear_bit_2(n, position):
    return n & ~(1 << position)


def read_bit_2(n, position):
    return n & (1 << position) >> position

