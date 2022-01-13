def maxSubsetSumNoAdjacent(array):
	if len(array) <= 2:
		return max(array, default=0)
	cache = [0, array[0], array[1]]
	for idx in range(2, len(array)):
		new_value = array[idx] + max(cache[len(cache) - idx - 3], cache[len(cache) - idx - 4])
		cache.append(new_value)
	return max(cache[-1], cache[-2])