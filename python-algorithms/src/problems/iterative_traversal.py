class Tree:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def iterativeInOrderTraversal(tree, callback):
	stack = [tree]
	while stack:
		node = stack.pop()
		while node.left:
			stack.append(node)
			node = node.left
		callback(node)
		if node.right:
			stack.append(node.right)

t = Tree(1, Tree(2, Tree(4, None, Tree(9))), Tree(3, Tree(6), Tree(7)))

iterativeInOrderTraversal(t, lambda node: print(node.value))