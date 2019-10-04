def insertionSort(array):
    copy = array[:]
    for i in range(len(copy)):
        j = i
        while j > 0 and copy[j] < copy[j - 1]:
            copy[j], copy[j-1] = copy[j-1], copy[j]
            j-=1
    return copy