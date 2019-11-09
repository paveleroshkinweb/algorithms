class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if self.adjacency_list.get(vertex) is not None:
            raise Exception('Such vertex already exist!')
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1] = (self.adjacency_list.get(vertex1) or []) + [vertex2]
        self.adjacency_list[vertex2] = (self.adjacency_list.get(vertex2) or []) + [vertex1]

    def remove_edge(self, vertex1, vertex2):
        list1, list2 = self.adjacency_list.get(vertex1), self.adjacency_list.get(vertex2)
        if list1 is None or list2 is None:
            raise Exception('There is no such edge!')
        index1, index2 = list1.index(vertex2), list2.index(vertex1)
        list1.pop(index1)
        list2.pop(index2)

    def get_all_vertexes(self):
        return self.adjacency_list.keys()

    def get_vertex_environment(self, vertex):
        return self.adjacency_list.get(vertex)

    def is_adjacent_vertexes(self, vertex1, vertex2):
        vertex1_environment = self.get_vertex_environment(vertex1)
        if vertex1_environment is None:
            return False
        return vertex2 in vertex1_environment

    def breadth_first_search(self):
        if len(self.adjacency_list) == 0:
            return
        vertices = list(self.adjacency_list)
        queue = [vertices[0]]
        used_vertices = set()
        while len(queue) > 0:
            vertex = queue.pop(0)
            childes = self.adjacency_list[vertex]
            for child in childes:
                if child not in used_vertices and child not in queue:
                    queue.append(child)
            used_vertices.add(vertex)
            yield vertex
    
    def count_vertices(self):
        return len(self.adjacency_list)
