from itertools import islice


def kadanesAlgorithm(array):
    best_sum = array[0]
    current_sum = best_sum
    for element in islice(array, 1, None):
        potential_sum = current_sum + element
        if element < 0:
            if potential_sum > 0:
                current_sum = potential_sum
            else:
                best_sum = max(best_sum, potential_sum, element)
                current_sum = 0
        else:
            current_sum = potential_sum
            best_sum = max(best_sum, current_sum, element)
    return best_sum


def kadanesAlgorithm2(array):
    current_sum = array[0]
    best_sum = current_sum
    for element in islice(array, 1, None):
        current_sum = max(element, current_sum + element)
        best_sum = max(best_sum, current_sum)
    return best_sum