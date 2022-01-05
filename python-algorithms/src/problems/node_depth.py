def nodeDepths(root):
    depths = []
	nodeDepthHelper(root, 0, depths)
	return sum(depths)

def nodeDepthHelper(node, current_depth, depths):
	if not node:
		return
	depths.append(current_depth)
	nodeDepthHelper(node.left, current_depth + 1, depths)
	nodeDepthHelper(node.right, current_depth + 1, depths)