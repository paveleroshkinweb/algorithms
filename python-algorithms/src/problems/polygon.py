def check(polygon, i, j):
    if j == len(polygon) - 1 or i == len(polygon) - 1:
        return True
    if polygon[i][j+1] == 1:
        return True
    if polygon[i+1][j] == 1:
        return True
    return False


def is_correct_polygon(polygon):
    for i in range(len(polygon)):
        for j in range(len(polygon)):
            if polygon[i][j] == 1:
                is_correct_shoot = check(polygon, i, j)
                if not is_correct_shoot:
                    return "NO"
    return "YES"


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        polygon = []
        for _ in range(int(input())):
            polygon.append([int(e) for e in input()])
        results.append(is_correct_polygon(polygon))
    print("\n".join(results))