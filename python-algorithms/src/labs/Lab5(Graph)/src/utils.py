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


def kruskal(graph):
    total_cost = 0
    result_graph = Graph()
    sorted_edges = _sorted_edges(graph)
    for edge in sorted_edges:
        connected_components = result_graph.connected_components()
        if result_graph.is_edge_in_graph(edge[0]) or \
                not _is_vertices_in_different_components(connected_components, edge[0][0], edge[0][1]) and \
                    result_graph.is_vertex_in_graph(edge[0][0]) and result_graph.is_vertex_in_graph(edge[0][1]):
                        continue
        total_cost += edge[1]
        result_graph.add_edge(edge[0][0], edge[0][1], edge[1])
    return total_cost, result_graph


def _sorted_edges(graph):
    edges = graph.get_all_edges()
    edges.sort(key=lambda edge: edge[1])
    return edges


def _is_vertices_in_different_components(connected_components, vertex1, vertex2):
    for component in connected_components:
        if vertex1 in component and vertex2 in component:
            return False
    return True


def is_acyclic_graph(graph):
    if graph.count_vertices() <= 2:
        return True
    visited_vertices = set()
    vertices = list(graph.get_all_vertices())
    colors = {}
    previous_vertex = vertices[0]

    def is_acyclic_graph_helper(vertex):
        nonlocal previous_vertex
        colors[vertex] = True
        visited_vertices.add(vertex)
        for adjacent_vertex in graph.get_vertex_environment(vertex):
            if adjacent_vertex not in visited_vertices:
                previous_vertex = vertex
                return is_acyclic_graph_helper(adjacent_vertex)
            elif adjacent_vertex != previous_vertex and colors.get(adjacent_vertex):
                return False
        colors[vertex] = False
        return True

    return is_acyclic_graph_helper(vertices[0])
