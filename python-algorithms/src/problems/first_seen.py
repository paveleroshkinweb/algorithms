def firstDuplicateValue(array):
    used = set()
	for element in array:
		if element in used:
			return element
		used.add(element)
	return -1


def firstDuplicateValue2(array):
    for element in array:
        if array[element - 1] < 0:
            return element
        array[element - 1] *= -1
    return -1