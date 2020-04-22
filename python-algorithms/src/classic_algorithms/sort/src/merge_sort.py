def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    return merge_arrays(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge_arrays(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    result = []
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] > arr2[pointer2]:
            result.append(arr2[pointer2])
            pointer2 += 1
        else:
            result.append(arr1[pointer1])
            pointer1 += 1
    while pointer1 < len(arr1):
        result.append(arr1[pointer1])
        pointer1 += 1
    while pointer2 < len(arr2):
        result.append(arr2[pointer2])
        pointer2 += 1
    return result
