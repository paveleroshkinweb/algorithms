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

        def min_helper(node, index):
            if node is None:
                return None
            elif index == k:
                return node.value
            else:
                index += 1
                return min_helper(node.left, index)

        return min_helper(self.root, 0)

    def height_tree(self):

        def height_tree_helper(node):
            if node is None:
                return 0
            return 1 + max(height_tree_helper(node.left), height_tree_helper(node.right))

        return height_tree_helper(self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.multiple_insert([12, 9, 14, 8, 11, 13, 15, 7])
    print(bst.height_tree())