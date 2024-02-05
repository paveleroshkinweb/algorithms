def getParity1(n):
    parity = 1
    while n:
        if n & 1:
            parity = not parity
        n >>= 1
    return int(parity)


def getParity2(n):
    parity = 0
    while n:
        parity = not parity
        n = n & (n-1)
    return int(parity)


def getParity3(n):
    parity_precalculated = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    parity = 0
    while n:
        parity += parity_precalculated[n & 0b1111]
        n >>= 4
    return parity % 2


def addParity(n):
    parity = getParity3(n)
    n = (n << 1) + parity
    return n


def checkParity(n):
    parity = n & 1
    actualParity = getParity3(n >> 1)
    return parity == actualParity
