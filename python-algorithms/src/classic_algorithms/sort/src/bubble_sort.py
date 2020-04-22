def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(0, i + 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
