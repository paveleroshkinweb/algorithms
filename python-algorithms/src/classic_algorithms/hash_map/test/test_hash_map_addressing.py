import unittest
from hash_map_addressing import HashMapAddressing


class TestHashMapChains(unittest.TestCase):

    def test_put(self):
        map = HashMapAddressing(8)
        map.put(1, 2)
        map.put(2, 3)
        map.put(3, 4)
        map.put(4, 5)
        map.put(33, 6)
        map.put(35, 7)
        map.put(36, 10)
        map.put(55, 11)
        self.assertEqual(35, map.buckets[0].key)
        self.assertEqual(1, map.buckets[1].key)
        self.assertEqual(2, map.buckets[2].key)
        self.assertEqual(3, map.buckets[3].key)
        self.assertEqual(4, map.buckets[4].key)
        self.assertEqual(36, map.buckets[5].key)
        self.assertEqual(55, map.buckets[6].key)
        self.assertEqual(55, map.buckets[6].key)
        self.assertEqual(33, map.buckets[7].key)

    def test_get(self):
        map = HashMapAddressing(8)
        map.put(1, 2)
        map.put(2, 3)
        map.put(3, 4)
        map.put(4, 5)
        map.put(33, 6)
        map.put(35, 7)
        map.put(36, 10)
        map.put(55, 11)
        self.assertEqual(2, map.get(1))
        self.assertEqual(3, map.get(2))
        self.assertEqual(4, map.get(3))
        self.assertEqual(5, map.get(4))
        self.assertEqual(6, map.get(33))
        self.assertEqual(7, map.get(35))
        self.assertEqual(10, map.get(36))
        self.assertEqual(11, map.get(55))


if __name__ == 'main':
    unittest.main()
