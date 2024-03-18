_TRANSITIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_perimeter(cells):
    visited = set()
    queue = [cells[0]]
    perimeter = 0

    while queue:
        cell = queue.pop()

        if cell in visited:
            continue

        visited.add(cell)

        for transition_x, transition_y in _TRANSITIONS:
            next_cell = (cell[0] + transition_x, cell[1] + transition_y)
            if next_cell not in cells:
                perimeter += 1
                continue
            queue.append(next_cell)

    return perimeter


if __name__ == '__main__':
    cells = []
    for _ in range(int(input())):
        cell = tuple(map(int, input().split()))
        cells.append(cell)
    perimeter = find_perimeter(cells)
    print(perimeter)
