class UnionFind:

    def __init__(self, elements):
        self.parents = {key: key for key in elements}

    def find(self, element):
        if element not in self.parents:
            return None
        path = []
        while self.parents[element] != element:
            path.append(element)
            element = self.parents[element]
        for vertex in path:
            self.parents[vertex] = element
        return element

    def is_same_set(self, element1, element2):
        return self.find(element1) == self.find(element2)

    def union(self, element1, element2):
        if element1 not in self.parents or element2 not in self.parents:
            return None
        parent1, parent2 = self.parents[element1], self.parents[element2]
        self.parents[parent2] = parent1
        return parent1
