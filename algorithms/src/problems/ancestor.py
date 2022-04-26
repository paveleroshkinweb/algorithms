class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):

    def getNodeDepth(topAncestor, node):
        depth = 0
        while node != topAncestor:
            depth += 1
            node = node.ancestor
        return depth

    def normalizeNodes(descendantOne, depth1, descendantTwo, depth2):
        if depth1 == depth2:
            return descendantOne, descendantTwo
        node_to_normalize = descendantOne
        normalized = descendantTwo
        if depth1 < depth2:
            node_to_normalize = descendantTwo
            normalized = descendantOne
        for _ in range(abs(depth1 - depth2)):
            node_to_normalize = node_to_normalize.ancestor
        return node_to_normalize, normalized

    depth1 = getNodeDepth(topAncestor, descendantOne)
    depth2 = getNodeDepth(topAncestor, descendantTwo)
    node_one, node_two = normalizeNodes(descendantOne, depth1, descendantTwo, depth2)
    if node_one == node_two:
        return node_one
    while node_one is not None:
        parent1 = node_one.ancestor
        parent2 = node_two.ancestor
        if parent1 == parent2:
            return parent1
        node_one = parent1
        node_two = parent2


def getYoungestCommonAncestor2(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    path1 = []
    path2 = set()
    current1 = descendantOne
    current2 = descendantTwo
    while current1:
        path1.append(current1)
        current1 = current1.ancestor
	while current2:
		path2.add(current2)
		current2 = current2.ancestor
	for el in path1:
		if el in path2:
			return el
	return topAncestor