class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if self.adjacency_list.get(vertex) is not None:
            raise Exception('Such vertex already exist!')
        self.adjacency_list[vertex] = []

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.add_vertex(vertex)

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

    def get_all_vertices(self):
        return self.adjacency_list.keys()

    def get_vertex_environment(self, vertex):
        return self.adjacency_list.get(vertex) or []

    def is_adjacent_vertices(self, vertex1, vertex2):
        vertex1_environment = self.get_vertex_environment(vertex1)
        if vertex1_environment is None:
            return False
        return vertex2 in vertex1_environment

    def get_start_vertex(self):
        if len(self.adjacency_list) == 0:
            return None
        return list(self.adjacency_list)[0]

    def breadth_first_search(self):
        if len(self.adjacency_list) == 0:
            return
        start_vertex = self.get_start_vertex()
        queue = [start_vertex]
        used_vertices = set()
        while len(queue) > 0:
            vertex = queue.pop(0)
            childes = self.adjacency_list[vertex]
            for child in childes:
                if child not in used_vertices and child not in queue:
                    queue.append(child)
            used_vertices.add(vertex)
            yield vertex

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
        depth_first_search_helper(self.get_start_vertex())
        return vertices_list

    def count_vertices(self):
        return len(self.adjacency_list)