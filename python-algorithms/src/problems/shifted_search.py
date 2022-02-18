def shiftedBinarySearch(array, target):
    middle = find_middle(array)
    left_result = binary_search(array, 0, middle, target)
    if left_result != -1:
        return left_result
    return binary_search(array, middle, len(array) - 1, target)


def find_middle(array):
    pivot = array[0]
    left = 0
    right = len(array) - 1
    middle = right
    while left <= right:
        m = (left + right) // 2
        element = array[m]
        if pivot > element:
            middle = m
            right = m - 1
        else:
            left = m + 1
    return middle


def binary_search(array, left, right, target):
    while left <= right:
        middle = (left + right) // 2
        element = array[middle]
        if element == target:
            return middle
        elif element > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1
