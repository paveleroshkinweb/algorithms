def robot_problem(n):
    if n <= 2:
        return n
    matrix = create_matrix(n)
    return matrix[0][n - 1]


def create_matrix(n):
    matrix = [[None] * n for _ in range(n)]
    fill_matrix(matrix)
    return matrix


def fill_matrix(matrix):
    fill_init_elements(matrix)
    count_ways_for_each_cell(matrix)


def fill_init_elements(matrix):
    length = len(matrix)
    matrix[length - 1][0] = 0
    for i in range(0, length):
        matrix[i][0] = 1
        matrix[length - 1][i] = 1


def sum_matrix_elements(matrix):
    length = len(matrix)
    _range = range(0, length)
    matrix_sum = 0
    for i in _range:
        for j in _range:
            matrix_sum += matrix[i][j]
    return matrix_sum


def count_ways_for_each_cell(matrix):
    length = len(matrix)
    for i in range(1, length):
        for j in range(length - 2, -1, -1):
            matrix[j][i] = matrix[j+1][i] + matrix[j][i-1]