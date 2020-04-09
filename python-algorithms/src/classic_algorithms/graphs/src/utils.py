from graph_list import Graph
import sys
from copy import copy
import heapq


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
                edge_cost = graph.get_edge_cost((vertex, adjacent_vertex))
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


def find_euler_cycle(graph, start_vertex=None):
    if not _euler_cycle_exist(graph) or graph.count_vertices() == 0:
        return None
    copy_graph = copy(graph)
    start_vertex = start_vertex or graph.get_start_vertex()

    def find_euler_cycle_helper(vertex):
        euler_cycle = []
        stack = [vertex]
        while len(stack) > 0:
            peek_vertex = stack.pop()
            euler_cycle.append(peek_vertex)
            if copy_graph.get_vertex_degree(peek_vertex) > 0:
                peek_environment = copy_graph.get_vertex_environment(peek_vertex)
                next_vertex = peek_environment[0]
                copy_graph.remove_edge(peek_vertex, next_vertex)
                stack.append(next_vertex)
            else:
                for vertex in euler_cycle[1:]:
                    if copy_graph.get_vertex_degree(vertex) != 0:
                        euler_cycle = euler_cycle[0:1] + find_euler_cycle_helper(vertex) + euler_cycle[2:]
        return euler_cycle

    return find_euler_cycle_helper(start_vertex)


def _euler_cycle_exist(graph):
    return all(map(lambda vertex: graph.get_vertex_degree(vertex) % 2 == 0, graph.get_all_vertices()))


def dijkstra(graph, start_vertex):
    queue = [(0, [start_vertex], start_vertex)]
    result_paths = {}
    while len(queue) > 0:
        path_len, path, vertex = heapq.heappop(queue)
        result_path = result_paths.get(vertex)
        if result_path is not None:
            result_paths[vertex] = result_path if result_path[1] < path_len else (path, path_len)
        else:
            result_paths[vertex] = (path, path_len)
        for adjacent_vertex in graph.get_vertex_environment(vertex):
            if adjacent_vertex not in result_paths:
                edge_cost = graph.get_edge_cost((vertex, adjacent_vertex))
                heapq.heappush(queue, (edge_cost + path_len, path + [adjacent_vertex], adjacent_vertex))
    return result_paths
