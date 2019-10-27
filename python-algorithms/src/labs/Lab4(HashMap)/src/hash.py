import math


def hash1(key, size):
    return key % size


def hash2(key, size):
    return int(size * key * 0.1)


def hash3(key, size):
    return int(size * key * (math.sqrt(5) - 1) / 2)
