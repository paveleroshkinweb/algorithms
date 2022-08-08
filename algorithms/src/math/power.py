def pow(n, power):
    result = 1
    n_degree = n
    while power:
        if power & 1 == 1:
            result *= n_degree
        power >>= 1
        n_degree *= n_degree
    return result


def pow2(n, power):
    if power == 0:
        return 1
    if power == 1:
        return n
    if power & 1 == 0:
        return pow2(n, power // 2) ** 2
    return pow2(n, power-1) * n