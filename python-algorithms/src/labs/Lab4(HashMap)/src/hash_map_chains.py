from entry import Entry
from collections import deque
import hash


class HashMapChains:

    def __init__(self):
        self.size = 0
        self.capacity = 53
        self.buckets = [deque() for _ in range(self.capacity)]

    def put(self, key, value):
        index = hash.hash1(key, self.capacity)
        bucket = self.buckets[index]
        founded_entry = next((entry for entry in bucket if entry.key == key), None)
        if founded_entry is not None:
            founded_entry.value = value
        else:
            bucket.append(Entry(key, value))
            self.size += 1

    def get(self, key):
        index = hash.hash1(key, self.capacity)
        bucket = self.buckets[index]
        return next((entry.value for entry in bucket if entry.key == key), None)

