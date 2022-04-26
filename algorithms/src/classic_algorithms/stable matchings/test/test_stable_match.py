import unittest
from StableMatch import StableMatch
from stableMarriageProblem import stable_marriage_problem


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
        self.assertEqual(51, stable_match.total_efficiency(pairs_by_preferences))

    def test_stable_marriage_problem(self):
        man_p = [
            [1, 0, 2, 3],
            [2, 1, 0, 3],
            [3, 2, 1, 0],
            [1, 0, 3, 2],
        ]
        girl_p = [
            [2, 3, 0, 1],
            [0, 2, 3, 1],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
        ]
        self.assertDictEqual({1: 0, 3: 2, 2: 1, 0: 3}, stable_marriage_problem(man_p, girl_p))
