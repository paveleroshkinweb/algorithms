def find_pairs(arr, l, r):
    arr.sort()
    count = 0
    for i in range(0, len(arr) - 1):
        left = binary_left_search(arr, i, l, r)
        right = binary_right_search(arr, i, l, r)
        if left != -1 and right != -1:
            count += right - left + 1

    return count


def binary_left_search(arr, i, l, r):
    left = i + 1
    right = len(arr) - 1
    potential = -1
    while left <= right:
        middle = (left + right) // 2
        subsum = arr[i] + arr[middle]
        if subsum >= l:
            potential = middle if l <= subsum <= r else potential
            right = middle - 1
        else:
            left = middle + 1
    return potential


def binary_right_search(arr, i, l, r):
    left = i + 1
    right = len(arr) - 1
    potential = -1
    while left <= right:
        middle = (left + right) // 2
        subsum = arr[i] + arr[middle]
        if subsum <= r:
            potential = middle if l <= subsum <= r else potential
            left = middle + 1
        else:
            right = middle - 1
    return potential


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _, l, r = [int(e) for e in input().split(' ')]
        arr = [int(e) for e in input().split(' ')]
        results.append(find_pairs(arr, l, r))
    print("\n".join(map(str, results)))
