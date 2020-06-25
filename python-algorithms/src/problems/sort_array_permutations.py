def sort_array_permutations(array):
    start = end = 0
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            start = i
            while i < len(array)-1 and array[i] > array[i+1]:
                i += 1
            end = i
            break
    array = array[0: start] + list(reversed(array[start:end+1])) + array[end+1:]
    is_sorted = all(
        array[i] <= array[i+1]
        for i in range(len(array) - 1)
    )
    return 'yes' + '\n' + str(start + 1) + ' ' + str(end + 1) if is_sorted else 'no'


if __name__ == '__main__':
    _ = input()
    array = [int(e) for e in input().split()]
    print(sort_array_permutations(array))