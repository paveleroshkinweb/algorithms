def slow_power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n

    return n * slow_power(n, p -1)


def quick_power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n

    if p % 2 == 0:
        return quick_power(n * n, p // 2)

    return n * quick_power(n, p - 1)

