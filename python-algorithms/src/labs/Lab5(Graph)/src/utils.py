def is_graph_connected(graph):
    return len(list(graph.breadth_first_search())) == graph.count_vertices()

