import unittest
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_extract(self):
        queue = PriorityQueue()
        queue.insert((5, 1))
        queue.insert((6, 5))
        queue.insert((3, 4))
        queue.insert((2, 7))
        queue.insert((1, 10))
        queue.insert((14, 11))
        self.assertEqual(14, queue.extract())
        self.assertEqual(1, queue.extract())
        self.assertEqual(2, queue.extract())
        self.assertEqual(6, queue.extract())
        self.assertEqual(3, queue.extract())
        self.assertEqual(5, queue.extract())