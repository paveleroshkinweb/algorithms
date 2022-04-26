def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if middle == array[middle]:
            result = middle
            right = middle - 1
        elif middle < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return result
