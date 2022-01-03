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