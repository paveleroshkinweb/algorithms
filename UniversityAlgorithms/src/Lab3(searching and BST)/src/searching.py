def linear_search(array, element):
    for i in range(0, len(array)):
        if array[i] == element:
            return i
    return -1


def search(array, element, getMid):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = getMid(left, right)
        if mid >= len(array):
            return -1
        elif array[mid] == element:
            return mid
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search(array, element):
    get_mid = lambda left, right: int((left + right) / 2)
    return search(array, element, get_mid)


def interpolation_search(array, element):
    get_mid = lambda left, right: int(left + (element - array[left]) * (right - left) / (array[right] - array[left]))
    return search(array, element, get_mid)
