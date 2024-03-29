from collections import defaultdict


_DIRECTIONS = [
    [(0, 1), (1, 0), (1, 1)],
    [(0, 1), (-1, 0), (-1, 1)]
]


def find_squre_coordinates(coordinates):
    x_map = defaultdict(lambda: set())

    for x, y in coordinates:

        x_map[x].add(y)

    extra_points = [None] * 3

    for x, y in coordinates:
        
        for coeff in range(1, 2001):

            for direction in _DIRECTIONS:

                potential_extra_points = []

                for x_shift, y_shift in direction:
                    new_x = x + x_shift * coeff
                    new_y = y + y_shift * coeff

                    if new_y not in x_map[new_x]:
                        potential_extra_points.append((new_x, new_y))
                
                if len(potential_extra_points) <= len(extra_points):
                    extra_points = potential_extra_points.copy()

                if len(extra_points) == 0:
                    return extra_points

    return extra_points



if __name__ == '__main__':
    coordinates = []
    for _ in range(int(input())):
        coordinates.append(tuple(map(int, input().split())))

    sq_coordinates = find_squre_coordinates(coordinates)
    print(len(sq_coordinates))
    print("\n".join(f"{coordinate[0]} {coordinate[1]}" for coordinate in sq_coordinates))
