def find_peek(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle-1] < array[middle] and array[middle + 1] < array[middle]:
            return array[middle]
        elif array[middle-1] < array[middle] < array[middle+1]:
            left = middle + 1
        else:
            right = middle - 1