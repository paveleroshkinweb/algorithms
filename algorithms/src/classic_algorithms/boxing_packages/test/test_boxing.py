import unittest
import boxing


create_test_data = lambda data, expected: {'test_data': data, 'expected': expected}


class TestBoxing(unittest.TestCase):

    def test_next_fit(self):
        test_data = [
            create_test_data(
                [0.1, 0.2, 0.3, 0.7, 1, 0.8],
                [[0.1, 0.2, 0.3], [0.7], [1], [0.8]]
            ),
            create_test_data(
                [1, 1, 1, 1],
                [[1], [1], [1], [1]]
            ),
            create_test_data(
                [0.5, 0.6, 0.4, 0.3],
                [[0.5], [0.6, 0.4], [0.3]]
            ),
            create_test_data(
                [],
                []
            )
        ]
        for data in test_data:
            self.assertSequenceEqual(data['expected'], boxing.next_fit(data['test_data']))

    def test_first_fit(self):
        test_data = [
            create_test_data(
                [0.1, 1, 0.3, 0.6, 0.8, 1, 0.1, 0.5],
                [[0.1, 0.3, 0.6], [1], [0.8, 0.1], [1], [0.5]]
            ),
            create_test_data(
                [1, 1, 1, 1],
                [[1], [1], [1], [1]]
            ),
            create_test_data(
                [0.5, 0.6, 0.4, 0.3],
                [[0.5, 0.4], [0.6, 0.3]]
            ),
            create_test_data(
                [],
                [[]]
            )
        ]
        for data in test_data:
            self.assertSequenceEqual(data['expected'], boxing.first_fit(data['test_data']))

    def test_best_fit(self):
        test_data = [
            create_test_data(
                [0.5, 0.8, 0.1, 0.1, 0.6, 0.4],
                [[0.5], [0.8, 0.1, 0.1], [0.6, 0.4]]
            ),
            create_test_data(
                [1, 1, 1, 1],
                [[1], [1], [1], [1]]
            ),
            create_test_data(
                [0.5, 0.6, 0.4, 0.3],
                [[0.5, 0.3], [0.6, 0.4]]
            ),
            create_test_data(
                [],
                [[]]
            )
        ]
        for data in test_data:
            self.assertSequenceEqual(data['expected'], boxing.best_fit(data['test_data']))
