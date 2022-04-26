def subarraySort(array):
	current_max = array[0]
	indexes = [-1, -1]
	for i in range(1, len(array)):
		if array[i] < array[i-1]:
			if indexes[0] == -1:
				indexes = [i-1, i]
			else:
				indexes[1] = i
		else:
			if indexes[0] != -1 and array[i] <= current_max:
				indexes[1] = i
		current_max = max(current_max, array[i])
	if indexes[0] != -1:
		min_in = min(array[indexes[0]: indexes[1] + 1])
		for i in range(0, indexes[0]):
			if array[i] > min_in:
				indexes[0] = i
				break
	return indexes