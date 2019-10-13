from node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def insert_helper(node):
            if value == node.value:
                raise Exception('All values in BST should be unique!')
            elif value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    insert_helper(node.left)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    insert_helper(node.right)

        insert_helper(self.root)

    def multiple_insert(self, values=[]):
        for value in values:
            self.insert(value)

    def bypass_order(self):
        if self.root is None:
            return []

        def bypass_order_helper(node):
            result = []
            if node is None:
                return result
            result += bypass_order_helper(node.left)
            result.append(node.value)
            result += bypass_order_helper(node.right)
            return result

        return bypass_order_helper(self.root)

    def bypass_post_order(self):
        if self.root is None:
            return []

        def bypass_post_order_helper(node):
            result = []
            if node is None:
                return result
            result += bypass_post_order_helper(node.right)
            result.append(node.value)
            result += bypass_post_order_helper(node.left)
            return result

        return bypass_post_order_helper(self.root)

    def find(self, value):

        def find_helper(node):
            if node is None or node.value == value:
                return node
            elif node.value > value:
                return find_helper(node.left)
            else:
                return find_helper(node.right)

        return find_helper(self.root)

    def min(self, k):
        index = k

        def min_helper(node):
            nonlocal index
            if node is None:
                return None
            left_res = min_helper(node.left)
            if left_res is not None:
                return left_res
            index -= 1
            if index == 0:
                return node.value
            right_res = min_helper(node.right)
            if right_res is not None:
                return right_res

        return min_helper(self.root)

    def height_tree(self):

        def height_tree_helper(node):
            if node is None:
                return 0
            return 1 + max(height_tree_helper(node.left), height_tree_helper(node.right))

        return height_tree_helper(self.root)

    def left_rotation(self):
        if self.root is None or self.root.right is None:
            return
        old_root = self.root
        self.root = old_root.right
        old_root.right = self.root.left
        self.root.left = old_root

    def right_rotation(self):
        if self.root is None or self.root.left is None:
            return
        old_root = self.root
        self.root = old_root.left
        old_root.left = self.root.right
        self.root.right = old_root

    def __str__(self):
        if self.root is None:
            return '[]'
        queue = [self.root]
        result = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node is not None:
                result.append(str(current_node))
                queue.extend([current_node.left, current_node.right])
        return str(result)