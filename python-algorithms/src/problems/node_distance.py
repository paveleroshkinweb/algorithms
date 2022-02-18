class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		self.parent = None

def findNodesDistanceK(tree, target, k):
	node = findNode(tree, target)
	seen = set()
	queue = [(node, k)]
	distances = []
	while queue:
		node, distance = queue.pop()
		if not node or node in seen:
			continue
		seen.add(node)
		if distance == 0:
			distances.append(node.value)
		else:
			queue.append((node.left, distance - 1))
			queue.append((node.right, distance - 1))
			try:
				queue.append((node.parent, distance - 1))
			except Exception:
				pass
	return distances


def findNode(tree, target):
	queue = [(tree, None)]
	while queue:
		subtree, parent = queue.pop()
		if not subtree:
			continue
		subtree.parent = parent
		if subtree.value == target:
			return subtree
		queue.append((subtree.left, subtree))
		queue.append((subtree.right, subtree))
	return None