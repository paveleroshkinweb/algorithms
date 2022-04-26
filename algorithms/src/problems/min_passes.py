def minimumPassesOfMatrix(matrix):
    positive_indexes = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] > 0]
    passes = 0
    while positive_indexes:
        new_positive = []
        for element in positive_indexes:
            children = childs_around(element, matrix)
            for child in children:
                i, j = child
                if matrix[i][j] < 0:
                    matrix[i][j] *= -1
                    new_positive.append((i, j))
        if len(new_positive) > 0:
            passes += 1
        positive_indexes = new_positive
    all_positive = all(matrix[i][j] >= 0 for i in range(len(matrix)) for j in range(len(matrix[0])))
    if all_positive:
        return passes
    return -1


def childs_around(point, matrix):
    childs = []
    i, j = point
    if j > 0:
        childs.append((i, j - 1))
    if j < len(matrix[0]) - 1:
        childs.append((i, j + 1))
    if i > 0:
        childs.append((i - 1, j))
    if i < len(matrix) - 1:
        childs.append((i + 1, j))
    return childs


