from binary_heap import BinaryHeap


class PriorityQueue:

    def __init__(self):
        self.binary_heap = BinaryHeap(lambda a, b: a[1] < b[1])

    def insert(self, element):
        self.binary_heap.insert(element)

    def multiple_insert(self, elements):
        for element in elements:
            self.insert(element)

    def extract(self):
        element = self.binary_heap.extract()
        return element[0] if element else element
