import unittest
from StableMatch import StableMatch


class TestStableMatch(unittest.TestCase):

    def test_stable_pairs(self):
        preferences = [
            [1, 0, 2, 3, 4],
            [4, 1, 2, 3, 0],
            [2, 3, 1, 0, 4],
            [1, 4, 3, 2, 0],
            [2, 0, 4, 1, 3]]
        estimations = [
            [12, 8, 3, 5, 10],
            [11, 13, 7, 9, 10],
            [14, 10, 9, 5, 8],
            [13, 14, 10, 8, 11],
            [11, 13, 14, 9, 15]]
        stable_match = StableMatch(preferences, estimations)
        pairs_by_estimations = stable_match.get_stable_pairs_by_estimations()
        pairs_by_preferences = stable_match.get_stable_pairs_by_preferences()
        self.assertEqual({0: 4, 1: 0, 2: 3, 3: 1, 4: 2}, pairs_by_estimations)
        self.assertEqual(46, stable_match.total_efficiency(pairs_by_estimations))
        self.assertEqual(51, stable_match.total_efficiency(pairs_by_preferences));

