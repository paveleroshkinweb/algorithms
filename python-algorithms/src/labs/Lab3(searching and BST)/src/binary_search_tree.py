from node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            return

        def insert_helper(node):
            if value == node.value:
                raise Exception('All values in BST should be unique!')
            elif value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    self.size += 1
                else:
                    insert_helper(node.left)
            else:
                if node.right is None:
                    node.right = Node(value)
                    self.size += 1
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

    def find_parent(self, value):
        if self.root is None or self.root.value == value:
            return None

        def find_parent_helper(node):
            if node is None:
                return None
            elif value < node.value:
                if node.left and node.left.value == value:
                    return node
                else:
                    return find_parent_helper(node.left)
            else:
                if node.right and node.right.value == value:
                    return node
                else:
                    return find_parent_helper(node.right)

        return find_parent_helper(self.root)

    def min(self, index):
        stack = []
        current = self.root
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                index -= 1
                if index == 0:
                    return current.value
                current = current.right
        return None

    def height_tree(self):

        def height_tree_helper(node):
            if node is None:
                return 0
            return 1 + max(height_tree_helper(node.left), height_tree_helper(node.right))

        return height_tree_helper(self.root)

    def left_rotation(self, root_value):
        node = self.find(root_value)
        node_parent = self.find_parent(root_value)
        if node is None or node.right is None:
            return
        old_sub_root = node
        node = old_sub_root.right
        old_sub_root.right = node.left
        node.left = old_sub_root
        if node_parent is None:
            self.root = node
        else:
            node_parent.left = node
        return node

    def right_rotation(self, root_value):
        node = self.find(root_value)
        node_parent = self.find_parent(root_value)
        if node is None or node.left is None:
            return
        old_sub_root = node
        node = old_sub_root.left
        old_sub_root.left = node.right
        node.right = old_sub_root
        if node_parent is None:
            self.root = node
        else:
            node_parent.right = node
        return node

    def dsw_balance(self):

        def create_backbone():
            current_node = self.root
            while current_node is not None:
                if current_node.left is not None:
                    node = self.right_rotation(current_node.value)
                    current_node = node
                else:
                    current_node = current_node.right

        def balance_backbone():
            leaves = get_bottom_expected_nodes()

        def get_bottom_expected_nodes():
            count = 0
            for i in range(0, self.height_tree()):
                count += 2**i
            return self.size - count

        create_backbone()
        balance_backbone()



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


