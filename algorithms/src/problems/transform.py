from heapq import heapify, heappush, heappop

def transformation(numbers):
    counter = {}
    for n in numbers:
        counter[n] = counter.get(n, 0) + 1
    items = [v * -1 for v in counter.values()]
    heapify(items)
    while len(items) > 1:
        peek1, peek2 = heappop(items), heappop(items)
        peek1 += 1
        peek2 += 1
        if peek1 != 0:
            heappush(items, peek1)
        if peek2 != 0:
            heappush(items, peek2)
    if len(items) > 0:
        return -items[0]
    return 0
