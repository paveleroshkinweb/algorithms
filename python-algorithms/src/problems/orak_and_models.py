def max_models(weights):
    cache = {i: 1 for i in range(1, len(weights) + 1)}
    for i in range(1, len(weights) + 1):
        for j in range(i * 2, len(weights) + 1, i):
            if weights[j-1] > weights[i-1]:
                cache[j] = max(cache[j], cache[i] + 1)
    return max(cache.values())


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        weights = [int(el) for el in input().split()]
        results.append(str(max_models(weights)))
    print('\n'.join(results))