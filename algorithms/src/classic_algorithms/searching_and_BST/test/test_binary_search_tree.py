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
        self.assertEqual([None, None], bst.find_node_with_parent(6))
        arr1 = bst.find_node_with_parent(2)
        self.assertEqual(2, arr1[0].value)
        self.assertEqual(None, arr1[1])
        arr2 = bst.find_node_with_parent(1)
        self.assertEqual(1, arr2[0].value)
        self.assertEqual(2, arr2[1].value)
        arr3 = bst.find_node_with_parent(4)
        self.assertEqual(4, arr3[0].value)
        self.assertEqual(3, arr3[1].value)

    def test_min(self):
        bst = BinarySearchTree()
        bst.multiple_insert([12, 9, 14, 8, 11, 13, 15, 7])
        self.assertEqual(9, bst.min(3).value)
        self.assertEqual(8, bst.min(2).value)
        self.assertEqual(7, bst.min(1).value)
        self.assertEqual(None, bst.min(10))

    def test_height_tree(self):
        bst = BinarySearchTree()
        bst.multiple_insert([12, 9, 14, 8, 11, 13, 15, 7])
        self.assertEqual(4, bst.height_tree(bst.root))

    def test_balance(self):
        bst1 = BinarySearchTree()
        bst1.multiple_insert([1, 2, 3, 4, 5, 6, 7, 8])
        bst1.balance()
        self.assertEqual(True, bst1.is_balanced())
        bst2 = BinarySearchTree()
        bst2.multiple_insert([8, 7, 6, 5, 4, 3, 2, 1])
        bst2.balance()
        self.assertEqual(True, bst2.is_balanced())
        bst3 = BinarySearchTree()
        bst3.multiple_insert([10, 9, 11])
        bst3.balance()
        self.assertEqual(True, bst3.is_balanced())

    def test_remove(self):
        bst = BinarySearchTree()
        bst.multiple_insert([6, 4, 5, 3, 2, 11])
        bst.remove(2)
        self.assertEqual(None, bst.find_node_with_parent(3)[0].left)
        bst.remove(4)
        self.assertEqual(None, bst.find_node_with_parent(3)[0].left)
        self.assertEqual(3, bst.find_node_with_parent(5)[0].left.value)
        self.assertRaises(Exception, bst.remove(5000))
        bst.remove(11)
        bst.remove(3)
        bst.remove(5)
        self.assertEqual(None, bst.find_node_with_parent(11)[0])
        self.assertEqual(None, bst.find_node_with_parent(3)[0])
        bst.remove(6)
        self.assertEqual(None, bst.root)


if __name__ == 'main':
    unittest.main()
