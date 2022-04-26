def getPermutations(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [[array[0]]]
    permutations = multipleMix(array[0], getPermutations(array[1:]))
    return permutations


def multipleMix(element, arrays):
    permutations = []
    for array in arrays:
        permutations += mix(element, array)
    return permutations


def mix(element, array):
    permutations = []
    for position in range(len(array) + 1):
        copy = array[:]
        copy.insert(position, element)
        permutations.append(copy)
    return permutations

