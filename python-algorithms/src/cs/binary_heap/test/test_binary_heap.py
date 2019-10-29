import unittest

from binary_heap import MaxBinaryHeap


class TestMaxBinaryHeap(unittest.TestCase):

    def test_insert(self):
        bh = MaxBinaryHeap()
        bh.insert(3)
        bh.insert(3)
        bh.insert(2)
        self.assertSequenceEqual([3, 3, 2], bh.values)
        bh.insert(4)
        self.assertSequenceEqual([4, 3, 2, 3], bh.values)

    def test_extract_max(self):
        bh = MaxBinaryHeap()
        bh.insert(4)
        bh.insert(1)
        bh.insert(1)
        bh.insert(3)
        bh.insert(3)
        bh.insert(2)
        bh.insert(2)
        self.assertEqual(4, bh.extract_max())
        self.assertEqual(3, bh.extract_max())
        self.assertEqual(3, bh.extract_max())
        self.assertEqual(2, bh.extract_max())
        self.assertEqual(2, bh.extract_max())
        self.assertEqual(1, bh.extract_max())
        self.assertEqual(1, bh.extract_max())


if __name__ == 'main':
    unittest.main()
