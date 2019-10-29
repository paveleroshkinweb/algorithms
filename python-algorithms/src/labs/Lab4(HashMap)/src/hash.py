import math


def hash1(key, size):
    return key % size


def hash2(key, size):
    return int(size * math.modf(key * 0.1)[0])


def hash3(key, size):
    return int(size * math.modf(key * (math.sqrt(5) - 1) / 2)[0])


def double_hash(key, size, i=1):
    return (hash.hash1(key, size) + i * hash.hash3(key, size)) % size
