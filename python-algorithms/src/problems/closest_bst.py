def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, tree.value)

def findClosestValueHelper(node, target, current_closest):
	if not node:
		return current_closest
	diff = target - node.value
	if abs(diff) < abs(target - current_closest):
		current_closest = node.value
	if diff == 0:
		return node.value
	if diff < 0:
		return findClosestValueHelper(node.left, target, current_closest)
	return findClosestValueHelper(node.right, target, current_closest)