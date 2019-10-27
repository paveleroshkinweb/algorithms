from entry import Entry
from collections import deque
import hash


class HashMapChains:

    def __init__(self):
        self.capacity = 32
        self.keys_set = set()
        self.buckets = [deque() for _ in range(self.capacity)]

    def put(self, key, value):
        if key in self.keys_set:
            raise Exception('Element with such key already exist!')
        new_entry = Entry(key, value)
        index = hash.hash1(key, self.capacity)
        self.buckets[index].append(new_entry)
        self.keys_set.add(key)

    def get(self, key):
        index = hash.hash1(key, self.capacity )
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

    def get_keys(self):
        return self.keys_set.copy()

    def size(self):
        return len(self.keys_set)

