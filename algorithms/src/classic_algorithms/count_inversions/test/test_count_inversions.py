from count_inversions import count_inversions
import unittest


class TestCountInversions(unittest.TestCase):

    def test_count_inversions(self):
        array1 = [2, 4, 5, 6, 1, 3]
        array2 = [1, 2, 3, 4, 0]
        array3 = [1, 2, 3, 4, 5]
        array4 = [5, 4, 3, 2, 1]
        array5 = [1]
        array6 = [1, 2]
        array7 = [2, 1]
        self.assertEqual(7, count_inversions(array1))
        self.assertEqual(4, count_inversions(array2))
        self.assertEqual(0, count_inversions(array3))
        self.assertEqual(10, count_inversions(array4))
        self.assertEqual(0, count_inversions(array5))
        self.assertEqual(0, count_inversions(array6))
        self.assertEqual(1, count_inversions(array7))
