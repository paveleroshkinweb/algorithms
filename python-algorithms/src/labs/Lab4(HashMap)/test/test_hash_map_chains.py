import unittest
from hash_map_chains import HashMapChains


class TestHashMapChains(unittest.TestCase):

    def test_put(self):
        map = HashMapChains()
        map.put(1, 2)
        map.put(2, 3)
        map.put(3, 4)
        map.put(4, 5)
        map.put(33, 6)
        map.put(34, 7)
        self.assertEqual(map.buckets[1][0].value, 2)
        self.assertEqual(map.buckets[2][0].value, 3)
        self.assertEqual(map.buckets[3][0].value, 4)
        self.assertEqual(map.buckets[4][0].value, 5)
        self.assertEqual(map.buckets[1][1].value, 6)
        self.assertEqual(map.buckets[2][1].value, 7)

    def test_get(self):
        map = HashMapChains()
        map.put(1, 2)
        map.put(33, 3)
        map.put(10, 12)
        self.assertEqual(2, map.get(1))
        self.assertEqual(3, map.get(33))
        self.assertEqual(12, map.get(10))
        self.assertEqual(None, map.get(100))

    def test_get_keys(self):
        map = HashMapChains()
        self.assertSetEqual(set(), map.get_keys())
        map.put(1, 2)
        map.put(33, 3)
        map.put(10, 12)
        self.assertSetEqual({1, 33, 10}, map.get_keys())

    def test_size(self):
        map = HashMapChains()
        self.assertEqual(0, map.size())
        map.put(1, 2)
        map.put(33, 3)
        map.put(10, 12)
        self.assertEqual(3, map.size())


if __name__ == 'main':
    unittest.main()
