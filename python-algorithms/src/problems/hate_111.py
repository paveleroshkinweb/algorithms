def decomposition(n):
    if n % 11 == 0 or n % 111 == 0:
        return "YES"
    remainder = n % 11
    subpart = n - (remainder * 111)
    if subpart > 0 and subpart % 11 == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    results = []
    for _ in range(int(input().strip())):
        test_data = int(input())
        results.append(decomposition(test_data))
    print("\n".join(results))