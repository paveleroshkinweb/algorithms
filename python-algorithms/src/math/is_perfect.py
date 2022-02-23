def is_perfect(n):
    assert n >= 0
    if n <= 1:
        return True
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if n / i != i:
                s += (n / i)
        i += 1
    return s == n
