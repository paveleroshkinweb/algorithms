def best_count(row1, row2):
    solution1 = [None] * len(row1)
    solution2 = [None] * len(row2)
    solution1[-1] = row1[-1]
    solution2[-1] = row2[-1]
    for i in range(len(solution1) - 2, -1, -1):
        solution1[i] = max(row1[i] + solution2[i+1], solution1[i+1])
        solution2[i] = max(row2[i] + solution1[i+1], solution2[i+1])
    return max(solution1[0], solution2[0])


if __name__ == '__main__':
    _ = input()
    row1 = list(map(int, input().strip().split(' ')))
    row2 = list(map(int, input().strip().split(' ')))
    solution = best_count(row1, row2)
    print(solution)
