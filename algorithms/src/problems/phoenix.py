def to_str(res):
    if res == -1:
        return str(-1)
    return str(len(res)) + '\n' + ' '.join([str(el) for el in res])


def phoenix_solution(k, arr):
    elements = list(set(arr))
    if len(elements) > k:
        return -1
    result = []
    for i in range(len(arr)):
        result += elements + [1] * (k - len(elements))
    return result


if __name__ == '__main__':
    solution = ''
    for _ in range(int(input())):
        _, k = [int(i) for i in input().split(' ')]
        arr = [int(i) for i in input().split(' ')]
        solution += to_str(phoenix_solution(k, arr)) + '\n'
    print(solution)
