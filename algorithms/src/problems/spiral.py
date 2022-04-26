from math import ceil


def spiralTraverse(array):
    spiral = []
    length = len(array[0])
    cycles = min(ceil(length / 2), ceil(len(array) / 2))
    for cycle in range(cycles):

        if (length % 2 != 0 or len(array) % 2 != 0) and cycle == cycles - 1:
            if length < len(array):
                for idx in range(cycle, len(array) - cycle):
                    spiral.append(array[idx][cycle])
            else:
                for idx in range(cycle, length - cycle):
                    spiral.append(array[cycle][idx])
            break

        for idx in range(cycle, length - cycle):
            spiral.append(array[cycle][idx])

        for idx in range(cycle + 1, len(array) - cycle):
            spiral.append(array[idx][length - cycle - 1])

        for idx in range(length - cycle - 2, cycle - 1, -1):
            spiral.append(array[len(array) - cycle - 1][idx])

        for idx in range(len(array) - cycle - 2, cycle, -1):
            spiral.append(array[idx][cycle])

    return spiral