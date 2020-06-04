a = [int(s) for s in input().split()]
juice_worms = [int(s) for s in input().split()]


def get_worm_heaps(a, juice_worms):
    heaps = generate_heaps(a)
    juice_worm_heaps = [str(find_heap(heaps, worm)) for worm in juice_worms]
    return juice_worm_heaps


def generate_heaps(a):
    heaps = []
    left_border = 1
    right_border = 0
    for i in range(len(a)):
        right_border += a[i]
        heaps.append((left_border, right_border))
        left_border = right_border + 1
    return heaps


def find_heap(heaps, juice_worm):
    i = 0
    j = len(heaps) - 1
    while i <= j:
        middle = (i+j) // 2
        heap = heaps[middle]
        if heap[0] <= juice_worm <= heap[1]:
            return middle + 1
        elif heap[0] > juice_worm:
            j = middle - 1
        else:
            i = middle + 1
    return -1


print('\n'.join(get_worm_heaps(a, juice_worms)), sep='')