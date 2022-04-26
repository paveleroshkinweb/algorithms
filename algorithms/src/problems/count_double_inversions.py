def count_double_inversions(array):

    def helper(array):
        if len(array) <= 1:
            return array, 0
        middle = len(array) // 2
        left_array, right_array = array[:middle], array[middle:]
        left_sorted, left_inversions = helper(left_array)
        right_sorted, right_inversions = helper(right_array)
        merged_array, inversions = merge(left_sorted, right_sorted)
        return merged_array, inversions + left_inversions + right_inversions

    return helper(array)[1]


def merge(array1, array2):
    inversions = 0
    i = j = 0
    merged_array = []
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            if array1[i] > 2 * array2[j]:
                inversions += len(array1) - i
            else:
                inversions += len(array1) - bin_search(array1, i, array2[j])
            merged_array.append(array2[j])
            j += 1
        else:
            merged_array.append(array1[i])
            i += 1
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1
    while j < len(array2):
        merged_array.append(array2[j])
        j += 1
    return merged_array, inversions


def bin_search(array, start, element):
    left = start + 1
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] > 2*element >= array[middle - 1]:
            return middle
        elif array[middle] <= 2*element:
            left = middle + 1
        else:
            right = middle - 1
    return len(array)


def brute_force(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j] * 2:
                inversions += 1
    return inversions


