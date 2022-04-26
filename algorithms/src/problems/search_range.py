def searchForRange(array, target):
    left_range = -1
    right_range = -1

    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        element = array[middle]
        if element == target:
            left_range = middle
            right = middle - 1
        elif element < target:
            left = middle + 1
        else:
            right = middle - 1

    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        element = array[middle]
        if element == target:
            right_range = middle
            left = middle + 1
        elif element < target:
            left = middle + 1
        else:
            right = middle - 1

    return [left_range, right_range]