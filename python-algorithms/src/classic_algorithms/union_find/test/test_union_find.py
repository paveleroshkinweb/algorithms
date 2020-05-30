from union_find import UnionFind
import unittest


class TestUnionFind(unittest.TestCase):

    def test_union_find(self):
        elements = [1, 2, 3, 4, 6, 7, 8]
        u1 = UnionFind(elements)
        for e in elements:
            self.assertEqual(e, u1.find(e))
        new_parent = u1.union(1, 2)
        self.assertEqual(1, new_parent)
        new_parent = u1.union(3, 4)
        self.assertEqual(3, new_parent)
        new_parent = u1.union(2, 4)
        self.assertEqual(1, new_parent)
        self.assertEqual(1, u1.find(4))
        new_parent = u1.union(3, 4)
        self.assertEqual(1, new_parent)
        new_parent = u1.union(3, 8)
        self.assertEqual(1, new_parent)
        new_parent = u1.union(8, 3)
        self.assertEqual(1, new_parent)