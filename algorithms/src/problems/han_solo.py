def get_array():
    return [int(el) for el in input().split()]


def gcd(a, b, c=None):
    return ((a if b == 0 else gcd(b, a % b)) if c is None
            else gcd(gcd(a, b), gcd(a, c)))


def get_line_odds(point1, point2):
    A = point1[1] - point2[1]
    B = point2[0] - point1[0]
    C = point1[0]*point2[1] - point2[0]*point1[1]
    devider = gcd(A, B, C)
    return A / devider, B / devider, C / devider


def shots(gun_coordinate, enemies):
    lines = set()
    count_shots = 0
    for enemy in enemies:
        new_line = get_line_odds(gun_coordinate, enemy)
        if new_line not in lines:
            count_shots += 1
            lines.add(new_line)
    return count_shots


if __name__ == '__main__':
    n, *gun_coordinate = get_array()
    enemies = [get_array() for _ in range(n)]
    print(shots(gun_coordinate, enemies))
