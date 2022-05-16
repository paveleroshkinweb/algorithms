def twoNumberSum(array, targetSum):
    # Write your code here.
	sorted_array = sorted(array)
	left = 0
	right = len(sorted_array) - 1
	while left < right:
		current_left = sorted_array[left]
		current_right = sorted_array[right]
		current_sum = current_left + current_right
		if current_sum == targetSum:
			return [current_left, current_right]
		elif current_sum > targetSum:
			right -= 1
		else:
			left += 1
	return []


def allTwoNumberSum(array, targetSum):
	sorted_array = sorted(array)
	pairs = []
	for i in range(0, len(array) - 1):
		target = targetSum - sorted_array[i]
		if target < sorted_array[i]:
			continue
		left = i + 1
		right = len(sorted_array) - 1
		while left <= right:
			middle = (left + right) // 2
			if sorted_array[middle] == target:
				pairs.append([sorted_array[i], sorted_array[middle]])
				break
			elif sorted_array[middle] > target:
				right = middle - 1
			else:
				left = middle + 1
	return pairs
