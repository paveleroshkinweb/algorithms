def binaryTreeDiameter(tree):
    best = [0]
    binaryTreeDiameterHelper(tree, best)
    return best[0]


def binaryTreeDiameterHelper(tree, best):
    if tree is None:
        return 0
    left_best_including = binaryTreeDiameterHelper(tree.left, best)
    right_best_including = binaryTreeDiameterHelper(tree.right, best)
    current_best_including = 1 + max(left_best_including, right_best_including)
    current_best_parent = left_best_including + right_best_including
    best[0] = max(current_best_parent, best[0])
    return current_best_including