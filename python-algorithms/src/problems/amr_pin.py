import math


def find_min_steps(r, x0, y0, x1, y1):
    distance = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    return math.ceil(distance / (r * 2))


if __name__ == '__main__':
    r, x0, y0, x1, y1 = map(int, input().strip().split(' '))
    print(find_min_steps(r, x0, y0, x1, y1))