def pow(n, power):
    result = 1
    n_degree = n
    while power:
        if power & 1 == 1:
            result *= n_degree
        power >>= 1
        n_degree *= n_degree
    return result
