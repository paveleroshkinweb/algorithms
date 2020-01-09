from graph_list import Graph
import sys


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


def prim(graph: Graph):
    total_cost = 0
    result_graph = Graph()
    used_vertices = set()
    while len(used_vertices) != len(graph.get_all_vertices()):
        cost, min_edge = _find_min_edge_prim(graph, used_vertices)
        used_vertices.update(min_edge)
        result_graph.add_edge(min_edge[0], min_edge[1], cost)
        total_cost += cost
    return total_cost, result_graph


def _find_min_edge_prim(graph, used_vertices):
    min_edge_cost = sys.maxsize
    min_edge = None
    vertices = used_vertices if used_vertices != set() else graph.get_all_vertices()
    for vertex in vertices:
        for adjacent_vertex in graph.get_vertex_environment(vertex):
            if adjacent_vertex not in used_vertices:
                edge_cost = graph.get_edge_const((vertex, adjacent_vertex))
                if min_edge_cost > edge_cost:
                    min_edge_cost = edge_cost
                    min_edge = (vertex, adjacent_vertex)
    return min_edge_cost, min_edge