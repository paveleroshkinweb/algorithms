def find_path(coordinates):
    path = ''
    sorted_coordinates = sorted(coordinates, key=lambda coordinate: (coordinate[0], coordinate[1]))
    prev_coordinates = (0, 0)
    for curr_coordinates in sorted_coordinates:
        if curr_coordinates[1] < prev_coordinates[1]:
            return "NO"
        right_path = 'R' * (curr_coordinates[0]-prev_coordinates[0])
        top_path = 'U' * (curr_coordinates[1]-prev_coordinates[1])
        path += right_path + top_path
        prev_coordinates = curr_coordinates
    return "YES" + '\n' + path


if __name__ == '__main__':
    all_coordinates = []
    for _ in range(int(input())):
        coordinates = []
        for _ in range(int(input())):
            pair = [int(s) for s in input().split()]
            coordinates.append(pair)
        all_coordinates.append(coordinates)
    for c in all_coordinates:
        print(find_path(c))
