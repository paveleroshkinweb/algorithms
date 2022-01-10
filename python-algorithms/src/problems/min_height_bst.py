def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, left, right):
	if left > right:
		return
	middle = (left + right) // 2
	new_node = BST(array[middle])
	new_node.left = minHeightBstHelper(array, left, middle - 1)
	new_node.right = minHeightBstHelper(array, middle + 1, right)
	return new_node