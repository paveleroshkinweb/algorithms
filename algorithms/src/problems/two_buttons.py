def two_buttons(start, end):
    cache = get_cache(start)
    temp = start + 1
    while end not in cache:
        if temp % 2 == 0:
            cache[temp] = 1 + cache[temp / 2]
        else:
            cache[temp] = 2 + cache[(temp+1) / 2]
        temp += 1
    return cache[end]


def get_cache(start):
    cache = {i: start - i for i in range(1, start)}
    cache[start] = 0
    return cache


if __name__ == '__main__':
    n, m = [int(e) for e in input().split()]
    print(two_buttons(n, m))
