def find_less(arr1, arr2):
    arr1.sort()
    results = []
    for e in arr2:
        idx = binary_search_less(arr1, e)
        results.append(idx+1)
    return results


def binary_search_less(arr, target):
    left = 0
    right = len(arr) - 1
    idx = -1
    while left <= right:
        middle = (left + right) // 2
        element = arr[middle]
        if element <= target:
            idx = middle
            left = middle + 1
        else:
            right = middle - 1
    return idx


if __name__ == '__main__':
    _ = input()
    arr1 = [int(e) for e in input().split(' ')]
    arr2 = [int(e) for e in input().split(' ')]
    print(" ".join(map(str, find_less(arr1, arr2))))