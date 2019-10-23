class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def has_direct_child(self, node):
        return self.left == node or self.right == node

    def has_no_child(self):
        return self.left is None and self.right is None

    def count_children(self):

        def count_children_helper(node):
            if node is None:
                return 0
            return 1 + count_children_helper(node.left) + count_children_helper(node.right)

        return count_children_helper(self.left) + count_children_helper(self.right)

    def remove_child(self, child):
        if self.left == child:
            child.left = None
        else:
            child.right = None

    def __str__(self):
        return f'(value={self.value}, ' \
               f'left={None if not self.left else self.left.value}, ' \
               f'right={None if not self.right else self.right.value})'
