def cycleInGraph(edges):
    not_visited = set([i for i in range(len(edges))])
    while not_visited:
        vertex = not_visited.pop()
        not_visited.add(vertex)
        is_cycle = cycle_dfs(vertex, edges, not_visited)
        if is_cycle:
            return True
    return False


def cycle_dfs(start_vertex, graph, not_visited):
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in not_visited:
            return True
        not_visited.remove(vertex)
        stack += graph[vertex]
    # stack += list(set(graph[vertex]) & not_visited)
    return False

cycleInGraph([
    [1, 2],
    [2],
    []])