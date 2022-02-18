def largestRange(array):
    elements = set(array)
    largest_range = None
    while elements:
        element = elements.pop()
        prev_element = element - 1
        next_element = element + 1

        while prev_element in elements:
            elements.remove(prev_element)
            prev_element -= 1
        prev_element += 1

        while next_element in elements:
            elements.remove(next_element)
            next_element += 1
        next_element -= 1

        potential_range = [prev_element, next_element]
        if largest_range:
            largest_range = largest_range if first_greater(largest_range, potential_range) else potential_range
        else:
            largest_range = potential_range
    return largest_range


def first_greater(range1, range2):
    first_diff = range1[1] - range1[0]
    second_diff = range2[1] - range2[0]
    return first_diff > second_diff
