def productSumHelper(array, depth=1):
	total = 0
	for element in array:
		if isinstance(element, list):
			total += (depth + 1) * productSumHelper(element, depth + 1)
		else:
			total += element
	return total

def productSum(array):
    return productSumHelper(array)
