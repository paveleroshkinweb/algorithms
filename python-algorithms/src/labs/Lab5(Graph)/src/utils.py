def is_graph_connected(graph):
    return len(list(graph.breadth_first_search())) == graph.count_vertices()


def is_bipartite(graph):
    set1, set2, checked_edges = [set() for _ in range(3)]
    for vertex in graph.breadth_first_search():
        if vertex in set2:
            for v in set2:
                is_checked_edge = (v, vertex) in checked_edges or (vertex, v) in checked_edges
                if not is_checked_edge and graph.is_adjacent_vertices(v, vertex):
                    return False
                checked_edges.add((v, vertex))
                checked_edges.add((vertex, v))
        else:
            set1.add(vertex)
            set2.update(graph.get_vertex_environment(vertex))
    return True
