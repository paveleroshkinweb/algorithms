def eratosthenes_sieve(n):
    primes = [i for i in range(0, n+1)]
    primes[0] = primes[1] = None
    for i in range(len(primes)):
        if primes[i] is not None:
            for j in range(2 * i, len(primes), primes[i]):
                primes[j] = None
    return [prime for prime in primes if prime is not None]
