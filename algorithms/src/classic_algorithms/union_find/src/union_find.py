class UnionFind1:

    def __init__(self, elements):
        self.parents = {key: key for key in elements}

    def find(self, element):
        return self.parents[element]

    def is_same_set(self, element1, element2):
        return self.parents[element1] == self.parents[element2]

    def union(self, element1, element2):
        for key in self.parents:
            if self.parents[key] == element2:
                self.parents[key] = element1
        return element1


class UnionFind2:

    def __init__(self, elements):
        self.parents = {key: key for key in elements}

    def find(self, element):
        while self.parents[element] != element:
            element = self.parents[element]
        return element

    def is_same_set(self, element1, element2):
        return self.find(element1) == self.find(element2)

    def union(self, element1, element2):
        if element1 not in self.parents or element2 not in self.parents:
            return None
        parent1, parent2 = self.find(element1), self.find(element2)
        self.parents[parent2] = parent1
        return parent1


class UnionFind3:

    def __init__(self, elements):
        self.parents = {key: (key, 1) for key in elements}
