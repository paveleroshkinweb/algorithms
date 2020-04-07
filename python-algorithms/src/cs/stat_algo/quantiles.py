def get_quartiles(array: list):
    sorted_array = sorted(array)
    length = len(sorted_array)
    parts = [sorted_array[:length // 2 - 1], sorted_array, sorted_array[length // 2:]]
    quartiles = [get_median(part) for part in parts]
    return quartiles


def get_median(sorted_array):
    length = len(sorted_array)
    if length % 2 != 0:
        return sorted_array[length // 2]
    return (sorted_array[length // 2 - 1] + sorted_array[length // 2]) / 2