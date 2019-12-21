import unittest
from StableMatch import StableMatch


class TestStableMatch(unittest.TestCase):

    def test_gale_shepley(self):
        employees_ranks = [
            [1, 0, 3, 4, 2],
            [3, 1, 0, 2, 4],
            [0, 2, 1, 4, 3],
            [1, 2, 4, 0, 3],
            [1, 3, 0, 4, 2]]
        tasks_ranks = [
            [1, 2, 0, 4, 3],
            [0, 4, 3, 2, 1],
            [1, 4, 3, 2, 0],
            [0, 3, 1, 4, 2],
            [0, 2, 4, 3, 1]]
        solver1, solver2 = StableMatch(employees_ranks, tasks_ranks), StableMatch(tasks_ranks, employees_ranks)
        self.assertEqual({0: [2], 1: [0], 2: [3], 3: [1], 4: [4]}, solver1.get_stable_pairs()[0])
        self.assertEqual({0: [1], 1: [0], 2: [4], 3: [3], 4: [2]}, solver2.get_stable_pairs()[0])
