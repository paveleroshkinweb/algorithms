from collections import defaultdict


def get_array():
    arr = input().split(' ')
    return [int(el) for el in arr]


def normalize_array(array, divider):
    remaining = defaultdict(lambda: 0)
    cycles = 0
    for n in array:
        if n % divider != 0:
            key = divider - (n % divider)
            remaining[key] += 1
            cycles = max(cycles, remaining[key])
    rest = 0
    for r in remaining:
        if remaining[r] == cycles:
            rest = max(rest, r + 1)
    return max((cycles - 1) * divider, 0) + rest


if __name__ == '__main__':
    solutions = []
    for _ in range(int(input())):
        _, k = get_array()
        numbers = get_array()
        solutions.append(str(normalize_array(numbers, k)))
    print('\n'.join(solutions))
