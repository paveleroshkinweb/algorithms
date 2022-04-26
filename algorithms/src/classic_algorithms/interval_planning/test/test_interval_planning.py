from interval_planning import max_independent_intervals, intervals_distribution
from weight_inverval_planning import weight_interval_planning, weight_interval_planning_iter
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

    def test_weight_interval_planning(self):
        intervals1 = [
            ((1, 2), 3),
            ((1.5, 3), 4),
            ((3.5, 5), 6),
            ((4, 4.5), 2),
            ((4.25, 6), 1),
            ((4.5, 7), 5),
            ((5.5, 9), 7),
        ]
        intervals2 = [
            ((1, 3), 7),
            ((2, 4), 3),
            ((2.5, 5), 10),
            ((4, 10), 5)
        ]
        self.assertEqual(17, weight_interval_planning(intervals1))
        self.assertEqual(17, weight_interval_planning_iter(intervals1))
        self.assertEqual(12, weight_interval_planning(intervals2))
        self.assertEqual(12, weight_interval_planning_iter(intervals2))