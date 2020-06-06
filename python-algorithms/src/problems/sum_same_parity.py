def find_terms(n, k):
    if k == 1:
        return "YES", n
    if k > n or n % 2 != 0 and k % 2 == 0:
        return "NO"
    if k == n:
        return "YES", [str(1)]*n
    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
        res = [str(1)]*(k-1) + [str(n-k+1)]
        return "YES", ' '.join(res)
    if n % 2 == 0 and k*2 <= n:
        res = [str(2)]*(k-1) + [str(n - 2*(k-1))]
        return "YES", ' '.join(res)
    return "NO"


if __name__ == '__main__':
    pairs = []
    for _ in range(int(input())):
        pairs.append([int(s) for s in input().split()])
    results = [find_terms(n, k) for n, k in pairs]
    print(results)
