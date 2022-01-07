from collections import defaultdict


def threeNumberSum(array, targetSum):
	array.sort()
	sum2_cache = defaultdict(lambda: [])
	triplets = []
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			sum2_cache[array[i] + array[j]].append([array[i], array[j]])
	for element in array:
		diff = targetSum - element
		if diff in sum2_cache:
			duplets = sum2_cache[diff]
			for duplet in duplets:
				if element not in duplet and element < duplet[0]:
					triplets.append([element, *duplet])
	return triplets


def threeNumberSum2(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			current_sum = array[i] + array[left] + array[right]
			if current_sum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif current_sum < targetSum:
				left += 1
			else:
				right -= 1
	return triplets