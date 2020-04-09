import math

class MaxBinaryHeap:

    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        self.bubble_up()

    def bubble_up(self):
        value = self.values[-1]
        parent_index = (len(self.values) - 1) // 2
        new_element_index = len(self.values) - 1
        while self.values[parent_index] < value and new_element_index > 0:
            self.swap(parent_index, new_element_index)
            new_element_index = parent_index
            parent_index = (new_element_index - 1) // 2

    def show_max(self):
        return self.values[0] if len(self.values) > 0 else None

    def extract_max(self):
        if len(self.values) == 0:
            return None
        max_value = self.values[0]
        self.swap(0, -1)
        del self.values[-1]
        if len(self.values) > 0:
            self.bubble_down()
        return max_value

    def bubble_down(self):
        index = 0
        while True:
            value = self.values[index]
            indexes = {'left_child_index': 2 * index + 1, 'right_child_index': 2 * index + 2}
            elements_indexes_map = {}
            for index_name in indexes.keys():
                index_number = indexes[index_name]
                if self.is_valid_index(index_number):
                    elements_indexes_map[self.values[index_number]] = index_number
            if len(elements_indexes_map) == 0:
                return
            max_child = max(elements_indexes_map.keys())
            if max_child > value:
                max_child_index = elements_indexes_map[max_child]
                self.swap(index, max_child_index)
                index = max_child_index
            else:
                return

    def is_valid_index(self, index):
        return 0 <= index < len(self.values)

    def swap(self, i, j):
        [self.values[i], self.values[j]] = [self.values[j], self.values[i]]

    def size(self):
        return len(self.values)