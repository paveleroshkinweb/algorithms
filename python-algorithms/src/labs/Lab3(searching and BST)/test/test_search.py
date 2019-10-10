import unittest

from searching import linear_search, binary_search, interpolation_search


class TestSearch(unittest.TestCase):

    def test_search(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        testData = [
            {'element': 1, 'index': 0},
            {'element': 10, 'index': 9},
            {'element': 4, 'index': 3},
            {'element': 100, 'index': -1}
        ]
        for data in testData:
            self.assertEqual(data['index'], linear_search(array, data['element']))
            self.assertEqual(data['index'], binary_search(array, data['element']))
            self.assertEqual(data['index'], interpolation_search(array, data['element']))


if __name__ == 'main':
    unittest.main()
