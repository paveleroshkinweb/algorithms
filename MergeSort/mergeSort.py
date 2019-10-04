from helper import get_rand;
from insertionSort import insertionSort;
import time;

def mergeSort(array):
    if len(array) <= 6:
        return insertionSort(array)
    mid = int(len(array) / 2)
    return mergeArrays(mergeSort(array[0:mid]), mergeSort(array[mid:]))

def mergeArrays(array1, array2):
    result = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] > array2[j]:
            result.append(array2[j])
            j+=1
        else:
            result.append(array1[i])
            i+=1
    while i < len(array1):
        result.append(array1[i])
        i+=1
    while j < len(array2):
        result.append(array2[j])
        j+=1
    return result    

if __name__ == '__main__':
    length = 100
    average = 0
    for i in range(0, length):
        randomArray = get_rand(10**3);
        previousTime = time.time() * 1000;
        sortedArray = mergeSort(randomArray)
        currentTime = time.time() * 1000;
        difference = currentTime - previousTime;
        average += difference
    average /= length
    print(average)
