class MaxBinaryHeap:

    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        parent_index = (len(self.values) - 1) // 2
        new_element_index = len(self.values) - 1
        while self.values[parent_index] < value and new_element_index > 0:
            self.swap(parent_index, new_element_index)
            new_element_index = parent_index
            parent_index = (new_element_index - 1) // 2

    def swap(self, i, j):
        [self.values[i], self.values[j]] = [self.values[j], self.values[i]]

    def size(self):
        return len(self.values)


if __name__ == '__main__':
    heap = MaxBinaryHeap()
    heap.insert(100)
    heap.insert(19)
    heap.insert(18)
    heap.insert(105)
    heap.insert(25)
    heap.insert(21)
    print(heap.values)
