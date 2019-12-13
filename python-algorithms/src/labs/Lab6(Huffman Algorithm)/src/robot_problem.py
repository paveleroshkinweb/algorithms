def robot_problem(n):
    matrix = create_matrix(n)
    return matrix[0][n - 1]


def create_matrix(n):
    matrix = [[None] * n for _ in range(n)]
    fill_matrix(matrix)
    return matrix


def fill_matrix(matrix):
    length = len(matrix)
    for i in range(1, length):
        for j in range(length - 2, -1, -1):
            matrix[j][i] = (matrix[j + 1][i] or 1) + (matrix[j][i - 1] or 1)