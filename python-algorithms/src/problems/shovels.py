from math import sqrt, ceil


def find_shovel(n, k):
    if k >= n:
        return 1
    res = n
    for i in range(2, min(k, ceil(sqrt(n))) + 1):
        if n % i == 0:
            division = n // i
            if division <= k:
                return i
            res = min(res, division)
    return res


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split(' ')]
        results.append(str(find_shovel(n, k)))
    print("\n".join(results))
