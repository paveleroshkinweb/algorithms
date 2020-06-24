from oriented_graph import Graph
from collections import defaultdict


def grig(graph: Graph, start: int, end: int):
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


def grig_line(number):
    marks = {1: 1, 2: 1}
    for n in range(3, number+1):
        marks[n] = marks[n-1] + marks[n-2]
    return marks[number]
