def sort(array):
    sorted_array = sorted(array)
    flag = True
    result = []
    while sorted_array:
        result.append(str(sorted_array.pop() if flag else sorted_array.pop(0)))
        flag = not flag
    return reversed(result)


if __name__ == '__main__':
    arrays = []
    for _ in range(int(input())):
        _ = input()
        array = [int(s) for s in input().split()]
        arrays.append(array)
    result = [' '.join(sort(a)) for a in arrays]
    print('\n'.join(result))
