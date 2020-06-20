import unittest
from random import randint
from nearest_pair import nearest_points, brute_force


class TestNearestPair(unittest.TestCase):

    def test_nearest_pair(self):
        for _ in range(1000):
            points = list(set([(randint(-10000, 10000), randint(-10000, 10000)) for _ in range(100)]))
            self.assertEqual(brute_force(points), nearest_points(points))