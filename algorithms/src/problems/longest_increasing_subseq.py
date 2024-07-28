def find_longest_subseq(arr: list[int]) -> int:
    subsolutions = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                subsolutions[i] = max(subsolutions[i], subsolutions[j]+1)
    return max(subsolutions)
