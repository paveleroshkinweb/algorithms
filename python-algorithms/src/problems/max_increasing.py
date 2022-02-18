def maxSumIncreasingSubsequence(array):
    cache = [[array[i], [array[i]]] for i in range(len(array))]
    for i in range(len(array) - 2, -1, -1):
        for j in range(i + 1, len(array)):
            if array[j] > array[i]:
                new_sum = cache[j][0] + array[i]
                if new_sum > cache[i][0]:
                    cache[i][0] = new_sum
                    cache[i][1] = [array[i], *cache[j][1]]
    return max(cache, key=lambda c: c[0])

    