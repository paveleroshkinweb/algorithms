def threeNumberSort(array, order):
	count = [0, 0, 0]
	for el in array:
		for i in range(3):
			if el == order[i]:
				count[i] += 1
	index = 0
	for idx, counter in enumerate(count):
		if counter > 0:
			target = order[idx]
			for i in range(index, index + counter):
				array[i] = target
			index = i + 1
	return array
	# for idx, counter in enumerate(count):
	# 	for i in range(index, idx+counter):
	# 		array[i] = order[idx]
	# 	index = i
	# return array

print(threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))