def cycleInGraph(edges):
    colors = set()
    not_visited = set([i for i in range(len(edges))])
    while not_visited:
        vertex = not_visited.pop()
        cycle = is_cycle(vertex, edges, not_visited, colors)
        if cycle:
            return True
    return False


def is_cycle(vertex, graph, not_visited, colors):
    colors.add(vertex)
    for child in graph[vertex]:
        if child in not_visited:
            not_visited.remove(child)
            child_cycle = is_cycle(child, graph, not_visited, colors)
            if child_cycle:
                return True
        elif child in colors:
            return True
    colors.remove(vertex)
    return False