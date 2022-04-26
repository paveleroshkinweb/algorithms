def findThreeLargestNumbers(array):
    first_three_elements = list(reversed(sorted(array[:3])))
	for element in array[3:]:
		for i in range(3):
			if element > first_three_elements[i]:
				for j in range(2, i, -1):
					first_three_elements[j] = first_three_elements[j-1]
				first_three_elements[i] = element
				break
	return list(reversed(first_three_elements))