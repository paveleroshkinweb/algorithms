def find_min_rectangle(squares):
    min_x = min(squares, key=lambda item: item[0])
    min_y = min(squares, key=lambda item: item[1])

    max_x = max(squares, key=lambda item: item[0])
    max_y = max(squares, key=lambda item: item[1])

    return ((min_x[0], min_y[1]), (max_x[0], max_y[1]))


if __name__ == '__main__':
    squares = []
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        squares.append((x, y))

    left, right = find_min_rectangle(squares)

    print(left[0], left[1], right[0], right[1])
