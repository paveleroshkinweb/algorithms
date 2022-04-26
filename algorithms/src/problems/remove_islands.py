def removeIslands(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if visited[i][j]:
                continue
            if matrix[i][j] == 1:
                removeIsland((i, j), matrix, visited)
            visited[i][j] = True
    return matrix


def removeIsland(start_point, matrix, visited):
    stack = [start_point]
    border_exists = False
    island = []
    while stack:
        point = stack.pop()
        i, j = point
        if matrix[i][j] == 1 and is_border(point, matrix):
            border_exists = True
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        island.append(point)
        if i > 0:
            stack.append((i - 1, j))
        if i < len(matrix) - 1:
            stack.append((i + 1, j))
        if j > 0:
            stack.append((i, j - 1))
        if j < len(matrix[0]) - 1:
            stack.append((i, j + 1))
    if not border_exists:
        for i, j in island:
            matrix[i][j] = 0


def is_border(point, matrix):
    return point[0] == 0 or point[0] == len(matrix) - 1 or point[1] == 0 or point[1] == len(matrix[0]) - 1