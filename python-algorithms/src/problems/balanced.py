def heightBalancedBinaryTree(tree):
    return heightBalancedBinaryTreeHelper(tree, 0)[0]


def heightBalancedBinaryTreeHelper(tree, height):
    if tree is None:
        return True, 0

    left_balanced, left_height = heightBalancedBinaryTreeHelper(tree.left, height)
    if not left_balanced:
        return False, None
    right_balanced, rigth_height = heightBalancedBinaryTreeHelper(tree.right, height)
    if not right_balanced:
        return False, None
    if abs(left_height - rigth_height) > 1:
        return False, None
    new_height = 1 + max(left_height, rigth_height)
    return True, new_height