def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    i = 0
    while i < len(array):
        jumps += 1
        max_jump = array[i]
        if i + max_jump >= len(array) - 1:
            break
        new_index = i + 1
        for j in range(i + 1, i + max_jump + 1):
            if j + array[j] >= new_index + array[new_index]:
                new_index = j
        i = new_index

    return jumps