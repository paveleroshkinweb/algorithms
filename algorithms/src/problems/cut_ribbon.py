from collections import defaultdict


def cut_ribbon(n, parts):

    parts = list(set(parts))
    cache = defaultdict(lambda: float('-inf'))
    cache.update({part: 1 for part in parts})
    for number in range(min(parts) + 1, n + 1):
        _max = max([cache[number - part] for part in parts])
        if number in parts and _max == float('-inf'):
            continue
        cache[number] = 1 + _max
    return cache[n]


if __name__ == '__main__':
    data = [int(e) for e in input().split()]
    n = data[0]
    parts = data[1:]
    print(cut_ribbon(n, parts))