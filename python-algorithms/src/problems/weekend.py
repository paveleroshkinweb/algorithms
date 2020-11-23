def min_rest_days(days):
    cache = {-1: [0, 0, 0]}
    for i in range(len(days)):
        prev_cache = cache[i-1]
        if days[i] == 0:
            cache[i] = [float('inf'),
                        float('inf'),
                        min(prev_cache[0], prev_cache[1], prev_cache[2]) + 1]
        elif days[i] == 1:
            if i > 0 and days[i] == days[i-1]:
                prev_min = prev_cache[2]
            else:
                prev_min = min(prev_cache[0], prev_cache[2])
            cache[i] = [float('inf'),
                        prev_min,
                        min(prev_cache[0], prev_cache[1], prev_cache[2]) + 1]
        elif days[i] == 2:
            if i > 0 and days[i] == days[i-1]:
                prev_min = prev_cache[2]
            else:
                prev_min = min(prev_cache[1], prev_cache[2])
            cache[i] = [prev_min,
                        float('inf'),
                        min(prev_cache[0], prev_cache[1], prev_cache[2]) + 1]
        elif days[i] == 3:
            first = min(prev_cache[1], prev_cache[2])
            second = min(prev_cache[0], prev_cache[2])
            if i > 0:
                if days[i-1] == 1:
                    second = prev_cache[2]
                elif days[i-1] == 2:
                    first = prev_cache[2]
            cache[i] = [first,
                        second,
                        min(prev_cache[0], prev_cache[1], prev_cache[2]) + 1]
    return min(cache[len(days) - 1])


if __name__ == '__main__':
    _ = input()
    days = [int(el) for el in input().split()]
    print(min_rest_days(days))

