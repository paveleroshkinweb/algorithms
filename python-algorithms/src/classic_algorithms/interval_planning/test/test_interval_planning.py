from interval_planning import max_independent_intervals, intervals_distribution
import unittest


class TestIntervalPlanning(unittest.TestCase):

    def test_max_independent_intervals(self):
        intervals = [(9, 13), (12, 15), (14, 16)]
        self.assertEqual(2, len(max_independent_intervals(intervals)))
        intervals = [(9, 13), (12, 15), (14, 17), (16, 19), (18, 20)]
        self.assertEqual(3, len(max_independent_intervals(intervals)))

    def test_intervals_distribution(self):
        intervals = [(9, 13), (14, 17), (19, 25), (12, 15), (16, 19), (11, 13.5), (13.7, 16.5), (18, 21)]
        self.assertEqual(3, len(intervals_distribution(intervals)))
        intervals = [(9, 13), (14, 17), (19, 25), (11, 13.5), (13.7, 16.5), (18, 21)]
        self.assertEqual(2, len(intervals_distribution(intervals)))