def backpack_algo(arr: list[int], target) -> int:
    solutions = [[0] * (target+1) for _ in range(len(arr)+1)]

    for i in range(len(arr)):

        for j in range(0, target+1):
            if j < arr[i]:
                solutions[i+1][j] = solutions[i][j]
            else:
                solutions[i+1][j] = max(
                    solutions[i][j-arr[i]] + arr[i],
                    solutions[i][j]
                )
    return solutions[-1][-1]

