class Graph:

    def __init__(self):
        self.adjacency_list = {}
        self.costs = {}

    def add_vertex(self, vertex):
        if self.adjacency_list.get(vertex) is not None:
            raise Exception('Such vertex already exist!')
        self.adjacency_list[vertex] = []

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edge(self, vertex1, vertex2, cost=0):
        self.adjacency_list[vertex1] = (self.adjacency_list.get(vertex1) or []) + [vertex2]
        self.adjacency_list[vertex2] = self.adjacency_list.get(vertex2) or []
        self.costs[(vertex1, vertex2)] = cost

    def remove_edge(self, vertex1, vertex2):
        adjacency_list = self.adjacency_list.get(vertex1)
        vertex_index = adjacency_list.index(vertex2)
        adjacency_list.pop(vertex_index)

    def get_vertex_environment(self, vertex):
        return self.adjacency_list.get(vertex) or []

    def get_edge_cost(self, edge):
        return self.costs.get(edge)

    def get_start_vertices(self):
        if len(self.adjacency_list) == 0:
            return None
        vertices = set(self.adjacency_list.keys())
        result_set = set()
        for vertex in vertices:
            adjacency_list = self.get_vertex_environment(vertex)
            result_set = result_set.union(adjacency_list)
        difference = vertices.difference(result_set)
        if difference == set():
            return list(list(self.adjacency_list)[0])
        return difference

    def depth_first_search(self):

        def depth_first_search_helper(current_vertex):
            visited_vertices.add(current_vertex)
            vertices_list.append(current_vertex)
            for vertex in self.get_vertex_environment(current_vertex):
                if vertex not in visited_vertices:
                    depth_first_search_helper(vertex)

        if len(self.adjacency_list) == 0:
            return []
        visited_vertices = set()
        vertices_list = []
        start_vertices = self.get_start_vertices()
        for vertex in start_vertices:
            depth_first_search_helper(vertex)
        return vertices_list

    def get_all_vertices(self):
        return self.adjacency_list.keys()