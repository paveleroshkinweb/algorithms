def count_inversions(array):

    def count_inversions_helper(array):
        if len(array) <= 1:
            return 0, array
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]
        left_count, left_merged = count_inversions_helper(left_array)
        right_count, right_merged = count_inversions_helper(right_array)
        new_count, new_array = merge_and_count(left_merged, right_merged)
        return left_count + right_count + new_count, new_array

    return count_inversions_helper(array)[0]


def merge_and_count(left_array, right_array):
    count = 0
    result_array = []
    i = j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] > right_array[j]:
            result_array.append(right_array[j])
            count += len(left_array) - i
            j += 1
        else:
            result_array.append(left_array[i])
            i += 1
    while i < len(left_array):
        result_array.append(left_array[i])
        i += 1
    while j < len(right_array):
        result_array.append(right_array[j])
        j += 1
    return count, result_array
