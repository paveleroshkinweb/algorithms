def eratosthenes(n):
    sieve = list(range(2, n + 1))
    for i in sieve:
        if i > 0:
            for j in range(i + i - 2, len(sieve), i):
                sieve[j] = 0
    result = set([n**2 for n in sieve if n != 0])
    return result


if __name__ == '__main__':
    _ = input()
    prime_squared = eratosthenes(10**6)
    arr = ["YES" if int(el) in prime_squared else "NO" for el in input().split(' ')]
    print('\n'.join(arr))
