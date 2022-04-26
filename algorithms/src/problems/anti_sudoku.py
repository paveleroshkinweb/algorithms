def anti_sudoku(sudoku):
    points_to_change = [(0, 0), (3, 1), (6, 2), (1, 3), (4, 4), (7, 5), (2, 6), (5, 7), (8, 8)]
    for x, y in points_to_change:
        sudoku[x][y] = anti_number(sudoku[x][y])
    return '\n'.join([''.join([str(e) for e in arr]) for arr in sudoku])


def anti_number(number):
    return number + 1 if number < 9 else 1


if __name__ == '__main__':
    res = ''
    for _ in range(int(input())):
        sudoku = []
        for _ in range(9):
            sudoku.append([int(e) for e in list(input())])
        res += anti_sudoku(sudoku) + '\n'
    print(res, sep='')