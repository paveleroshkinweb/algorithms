def maxPathSum(tree):

    path_sum = tree.value

    def maxPathSumHelper(node):
        nonlocal path_sum
        if node is None:
            return 0
        left = maxPathSumHelper(node.left)
        right = maxPathSumHelper(node.right)
        subsum = max(node.value, node.value + max(left, right))
        path_sum = max(path_sum, subsum, left + right + node.value)
        return subsum

    left_result = maxPathSumHelper(tree.left)
    right_result = maxPathSumHelper(tree.right)
    return max(
        path_sum,
        left_result + right_result + tree.value,
        left_result + tree.value,
        right_result + tree.value
    )
