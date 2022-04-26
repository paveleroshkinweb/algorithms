from collections import defaultdict


def fourNumberSum(array, targetSum):
	pairs = defaultdict(lambda: [])
	quadruplets = []
	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			diff = targetSum - array[i] - array[j]
			for pair in pairs[diff]:
				quadruplets.append([*pair, array[i], array[j]])
		for k in range(0, i):
			pairs[array[k] + array[i]].append([array[k], array[i]])
	return quadruplets