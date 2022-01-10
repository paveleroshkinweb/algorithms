def findKthLargestValueInBst(tree, k):
	return findKthLargestValueInBstHelper(tree, [k])


def findKthLargestValueInBstHelper(tree, arr):
	if tree is None:
		return
	res1 = findKthLargestValueInBstHelper(tree.right, arr)
	if res1 is not None:
		return res1
	arr[0] -= 1
	if arr[0] == 0:
		return tree.value
	res2 = findKthLargestValueInBstHelper(tree.left, arr)
	if res2 is not None:
		return res2