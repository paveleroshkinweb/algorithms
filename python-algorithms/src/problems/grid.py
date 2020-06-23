from oriented_graph import Graph
from collections import defaultdict


def grid(graph: Graph, start: int, end: int):
    queue = [(vertex, start) for vertex in graph.get_vertex_environment(start)]
    marks = defaultdict(int)
    marks[start] = 1
    prev_values = {start: 0}

    while queue:
        vertex, parent = queue.pop(0)
        prev_values[vertex] = marks[vertex]
        marks[vertex] += marks[parent] - prev_values[parent]
        queue.extend([(v, vertex)
                      for v in graph.get_vertex_environment(vertex)
                      ])
    return marks[end]
