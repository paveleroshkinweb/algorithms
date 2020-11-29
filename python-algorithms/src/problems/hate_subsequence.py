def get_distance(binary_str):
    distance = [[binary_str[0], 1]]
    for i in range(1, len(binary_str)):
        if binary_str[i] == distance[-1][0]:
            distance[-1][1] += 1
        else:
            distance.append([binary_str[i], 1])
    return distance


def solution_headed(distance, bit):
    s = sum([el[1] for el in distance if el[0] == bit])
    solution = float('inf')
    prev_sum = 0
    for el in distance:
        if el[0] != bit:
            solution = min(solution, prev_sum + s)
            prev_sum += el[1]
        else:
            s -= el[1]
    return min(solution, sum([el[1] for el in distance if el[0] != bit]))


def solution(binary_str):
    distance = get_distance(binary_str)
    if len(distance) <= 2:
        return 0
    zero_headed = solution_headed(distance, '0')
    one_headed = solution_headed(distance, '1')
    return min(zero_headed, one_headed)


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        binary_str = input()
        results.append(str(solution(binary_str)))
    print('\n'.join(results))
