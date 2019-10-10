import unittest

from binary_search_tree import BinarySearchTree


class TestBST(unittest.TestCase):

    def test_insertion(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(2, bst.root.value)
        self.assertEqual(1, bst.root.left.value)
        self.assertEqual(3, bst.root.right.value)

    def test_multiple_insertion(self):
        bst = BinarySearchTree()
        bst.multiple_insert([2, 1, 3])
        self.assertEqual(2, bst.root.value)
        self.assertEqual(1, bst.root.left.value)
        self.assertEqual(3, bst.root.right.value)

    def test_bypass_order(self):
        bst = BinarySearchTree()
        ordered_array1 = bst.bypass_order()
        self.assertSequenceEqual([], ordered_array1)
        bst.insert(2)
        ordered_array2 = bst.bypass_order()
        self.assertSequenceEqual([2], ordered_array2)
        bst.insert(1)
        ordered_array3 = bst.bypass_order()
        self.assertSequenceEqual([1, 2], ordered_array3)
        bst.insert(3)
        ordered_array4 = bst.bypass_order()
        self.assertSequenceEqual([1, 2, 3], ordered_array4)

    def test_bypass_post_order(self):
        bst = BinarySearchTree()
        ordered_array1 = bst.bypass_post_order()
        self.assertSequenceEqual([], ordered_array1)
        bst.insert(2)
        ordered_array2 = bst.bypass_post_order()
        self.assertSequenceEqual([2], ordered_array2)
        bst.insert(1)
        ordered_array3 = bst.bypass_post_order()
        self.assertSequenceEqual([2, 1], ordered_array3)
        bst.insert(3)
        ordered_array4 = bst.bypass_post_order()
        self.assertSequenceEqual([3, 2, 1], ordered_array4)

    def test_find(self):
        bst = BinarySearchTree()
        bst.multiple_insert([2, 1, 3, 4])
        self.assertEqual(None, bst.find(6))
        self.assertEqual(2, bst.find(2).value)
        self.assertEqual(1, bst.find(1).value)
        self.assertEqual(3, bst.find(3).value)
        self.assertEqual(4, bst.find(4).value)

    def test_min(self):
        bst = BinarySearchTree()
        bst.multiple_insert([12, 9, 14, 8, 11, 13, 15, 7])
        self.assertEqual(7, bst.min(3))
        self.assertEqual(8, bst.min(2))
        self.assertEqual(9, bst.min(1))
        self.assertEqual(12, bst.min(0))
        self.assertEqual(None, bst.min(10))

    def test_height_tree(self):
        bst = BinarySearchTree()
        bst.multiple_insert([12, 9, 14, 8, 11, 13, 15, 7])
        self.assertEqual(4, bst.height_tree())


if __name__ == 'main':
    unittest.main()
