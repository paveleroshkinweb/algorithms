from collections import defaultdict


def match_twist(arr1, arr2):
    map2 = {arr2[i]: i for i in range(len(arr2))}
    buckets = defaultdict(lambda: 0)
    for index1 in range(len(arr2)):
        index2 = map2[arr1[index1]]
        diff = index1 - index2
        if diff < 0:
            diff += len(arr1)
        buckets[diff] += 1
    return max(buckets.values())


def get_arr():
    arr = input().split()
    return [int(el) for el in arr]


if __name__ == '__main__':
    _ = input()
    arr1, arr2 = get_arr(), get_arr()
    print(match_twist(arr1, arr2))