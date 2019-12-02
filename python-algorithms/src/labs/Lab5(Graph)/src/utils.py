from collections import deque


def is_graph_connected(graph):
    return len(list(graph.breadth_first_search())) == graph.count_vertices()


def is_bipartite(graph):
    vertex = graph.get_start_vertex()
    colors = {vertex: 1}
    visited_vertices = set([vertex])
    iteration_count = len(graph.get_vertex_environment(vertex))
    for current_vertex in graph.breadth_first_search():
        if current_vertex not in visited_vertices:
            visited_vertices.add(current_vertex)
            colors[current_vertex] = 1 - colors[vertex]
        elif colors[current_vertex] == colors[vertex] and current_vertex != vertex:
            return False
        if iteration_count == 0:
            vertex = current_vertex
            iteration_count = len(graph.get_vertex_environment(current_vertex))
        iteration_count -= 1
    return True


def find_euler_cycle(graph):
    if not is_euler_path_exists(graph):
        return []
    cycle = deque()
    path = deque()

    # visited_edges = set()
    # stack = [find_odd_power_vertex(graph) or graph.get_start_vertex()]
    # while len(stack) > 0:
    #     vertex = stack.pop(0)
    #     for adjacent_vertex in graph.get_vertex_environment(vertex):
    #         edge = (vertex, adjacent_vertex)
    #         if edge in visited_edges:
    #             stack.append(adjacent_vertex)
    #             visited_edges.remove(edge)
    #             break
    #     if len(stack) > 0 and vertex == stack[-1]:
    #         return stack[:-1]


# def find_odd_power_vertex(graph):
#     for vertex in graph.get_all_vertices():
#         if is_odd_vertex(vertex, graph):
#             return vertex


def is_odd_vertex(vertex, graph):
    return len(graph.get_vertex_environment(vertex)) % 2 != 0


def is_euler_path_exists(graph):
    for vertex in graph.get_all_vertices():
        if is_odd_vertex(vertex, graph):
            return False
    return True
