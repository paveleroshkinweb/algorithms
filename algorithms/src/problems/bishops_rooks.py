_BOARD_SIZE = 8
_CELLS_NUMBER = _BOARD_SIZE ** 2
_BISHOP_SIGN = 'B'
_ROOK_SIGN = 'R'

_BISHOP_TRANSITIONS = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
_ROOK_TRANSITIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def is_cell_outside_field(i, j):
    return i < 0 or i >= _BOARD_SIZE or j < 0 or j >= _BOARD_SIZE


def hit(hit_matrix, start_position, transition, bishops_positions, rooks_positions):
    i, j = start_position

    while not is_cell_outside_field(i, j):
        position = (i, j)
        
        if position != start_position and (position in bishops_positions or position in rooks_positions):
            hit_matrix[i][j] = 1
            return
        
        hit_matrix[i][j] = 1
        i += transition[0]
        j += transition[1]



def find_free_cells(bishops_positions, rooks_positions):
    hit_matrix = [[0] * _BOARD_SIZE for _ in range(_BOARD_SIZE)]

    for bishop_position in bishops_positions:
        for transition in _BISHOP_TRANSITIONS:
            hit(hit_matrix, bishop_position, transition, bishops_positions, rooks_positions)

    for rook_position in rooks_positions:
        for transition in _ROOK_TRANSITIONS:
            hit(hit_matrix, rook_position, transition, bishops_positions, rooks_positions)

    return _CELLS_NUMBER - sum(map(sum, hit_matrix))


if __name__ == '__main__':
    bishops_positions = set()
    rooks_positions = set()

    for i in range(_BOARD_SIZE):
        positions = input().strip()
        for j, position in enumerate(positions):
            if position == _BISHOP_SIGN:
                bishops_positions.add((i, j))
            elif position == _ROOK_SIGN:
                rooks_positions.add((i, j))

    free_cells = find_free_cells(bishops_positions, rooks_positions)
    print(free_cells)
