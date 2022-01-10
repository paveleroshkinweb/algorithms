def reconstructBst(arr):
    tree_root = BST(arr[0])
    stack = [tree_root]
    idx = 1
    while idx < len(arr):
        node = stack[-1]
        new_node = BST(arr[idx])
        if new_node.value < node.value:
            node.left = new_node
        else:
            prev_node = node
            current_node = node
            while stack and new_node.value >= current_node.value:
                prev_node = current_node
                current_node = stack.pop()
            if current_node.value <= new_node.value:
                current_node.right = new_node
            else:
                stack.append(current_node)
                prev_node.right = new_node
        stack.append(new_node)
        idx += 1
    return tree_root
