from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n - 2)


def generator_fibonacci(n):
    prev = 0
    next = 1
    for _ in range(0, n):
        yield prev
        prev, next = next, prev + next


