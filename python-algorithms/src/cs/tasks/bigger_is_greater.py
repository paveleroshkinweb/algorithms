def bigger_is_greater(string):
    number_arr = list(map(lambda char: ord(char), string))
    length = len(number_arr)
    current_swap_index, last_index = find_indexes(number_arr)
    if current_swap_index is None:
        return 'no answer'
    return string[0:current_swap_index] + \
           string[last_index] + \
           string[current_swap_index: last_index] + \
           '' if last_index + 1 == length else string[last_index + 1]


def find_indexes(number_arr):
    length = len(number_arr)
    for i in range(length - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if number_arr[j] < number_arr[i]:
                return j, i
    return None, None
