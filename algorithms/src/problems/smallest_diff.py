def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	pointer1 = 0
	pointer2 = 0
	smallestDiff = float('inf')
	smallestDiffPair = []
	while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
		element1 = arrayOne[pointer1]
		element2 = arrayTwo[pointer2]
		diff = abs(element1 - element2)
		if diff < smallestDiff:
			smallestDiff = diff
			smallestDiffPair = [element1, element2]
		if element1 < element2:
			pointer1 += 1
		else:
			pointer2 += 1
	return smallestDiffPair