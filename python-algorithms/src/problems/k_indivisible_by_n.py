import math


def find_k_indivisible_by_n(n, k):
    bucket = math.ceil(k / (n - 1))
    passed = (bucket - 1) * (n - 1)
    previous_divisible = (bucket - 1) * n
    return previous_divisible + (k - passed)


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        results.append(str(find_k_indivisible_by_n(*[int(s) for s in input().split()])))
    print('\n'.join(results), sep='')
