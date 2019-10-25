import unittest

from binary_heap import MaxBinaryHeap


class TestMaxBinaryHeap(unittest.TestCase):

    def test_insert(self):
        bh = MaxBinaryHeap()
        bh.insert(2)
        bh.insert(1)
        bh.insert(3)
        self.assertSequenceEqual([3, 2, 1], bh.values)
        bh.insert(4)
        self.assertSequenceEqual([4, 3, 1, 2], bh.values)

    def test_extract_max(self):
        bh = MaxBinaryHeap()
        bh.insert(2)
        bh.insert(1)
        bh.insert(3)
        bh.insert(5)
        bh.insert(4)
        self.assertEqual(5, bh.extract_max())
        self.assertEqual(4, bh.extract_max())
        self.assertEqual(3, bh.extract_max())
        self.assertEqual(2, bh.extract_max())
        self.assertEqual(1, bh.extract_max())


if __name__ == 'main':
    unittest.main()
