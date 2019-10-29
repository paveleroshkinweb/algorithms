from entry import Entry
from collections import deque
import hash


class HashMapAddressing:

    def __init__(self):
        self.capacity = 53
        self.buckets = [None] * self.capacity

    def put(self, key, value):
        index = hash.double_hash(key, self.capacity)
