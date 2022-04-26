import unittest

from binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def test_insert(self):
        bh = BinaryHeap(compare=lambda a, b: a < b)
        bh.insert(3)
        bh.insert(3)
        bh.insert(2)
        self.assertSequenceEqual([3, 3, 2], bh.values)
        bh.insert(4)
        self.assertSequenceEqual([4, 3, 2, 3], bh.values)

    def test_extract(self):
        bh = BinaryHeap(compare=lambda a, b: a < b)
        bh.insert(4)
        bh.insert(1)
        bh.insert(1)
        bh.insert(3)
        bh.insert(3)
        bh.insert(2)
        bh.insert(2)
        self.assertEqual(4, bh.extract())
        self.assertEqual(3, bh.extract())
        self.assertEqual(3, bh.extract())
        self.assertEqual(2, bh.extract())
        self.assertEqual(2, bh.extract())
        self.assertEqual(1, bh.extract())
        self.assertEqual(1, bh.extract())


if __name__ == 'main':
    unittest.main()
