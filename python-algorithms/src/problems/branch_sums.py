def branchSums(root):
    arr = []
	branchSumsHelper(root, arr, 0)
	return arr

def branchSumsHelper(node, array, current_sum):
	current_sum += node.value
	if node.left:
		branchSumsHelper(node.left, array, current_sum)
	if node.right:
		branchSumsHelper(node.right, array, current_sum)
	if not node.left and not node.right:
		array.append(current_sum)