def is_graph_connected(graph):
    return len(list(graph.breadth_first_search())) == graph.count_vertices()


def is_bipartite(graph):
    start_vertex = graph.get_start_vertex()
    queue = [start_vertex]
    used_vertices = set()
    current_color = False
    colors = {}
    parts = {True: [], False: []}
    while len(queue) > 0:
        vertex = queue.pop()
        colors[vertex] = current_color
        parts[current_color].append(vertex)
        current_color = not current_color
        used_vertices.add(vertex)
        adjacent_vertices = graph.get_vertex_environment(vertex)
        for adjacent_vertex in adjacent_vertices:
            if adjacent_vertex in used_vertices and colors[vertex] == colors[adjacent_vertex]:
                return False, []
            elif adjacent_vertex not in used_vertices and adjacent_vertex not in queue:
                queue.append(adjacent_vertex)
    return True, (parts[True], parts[False])

