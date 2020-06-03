numbers = [int(n) for n in input().split()]


def get_zero_data(numbers):
    zero_data = []
    i = 0
    while i < len(numbers):
        if numbers[i] == 0:
            data = [i, 1, 0]
            i += 1
            while i < len(numbers) and numbers[i] == 0:
                data[1] += 1
                i += 1
            zero_data.append(data)
        i += 1
    return zero_data


def get_best_solution(numbers, zero_data):
    if not zero_data:
        return len(numbers) - 1
    best_solution, solution = [*zero_data[0]], [*zero_data[0]]
    for z_data in zero_data[1:]:
        cur_ones_between = z_data[0] - solution[0] - solution[1] - solution[-1]
        if solution[-1] + cur_ones_between < solution[1]:
            best_solution = max(best_solution, solution, key=lambda s: s[1] - s[-1])[:]
            solution[1] += z_data[1]
            solution[-1] += cur_ones_between
        else:
            solution = z_data
    best_solution = max(best_solution, solution, key=lambda s: s[1] - s[-1])
    return sum(numbers) + best_solution[1] - best_solution[2]


zero_data = get_zero_data(numbers)
print(get_best_solution(numbers, zero_data))