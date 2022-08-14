from heapq import heappush, heappop, heapify
import random


# N*logN
def k_stat(arr, position):
    assert position < len(arr)
    return sorted(arr)[position]


# N*log(k**2)
def k_stat2(arr, position):
    assert position < len(arr)
    heap = [-arr[idx] for idx in range(position+1)]
    heapify(heap)
    for idx in range(position+1, len(arr)):
        heappop(heap)
        heappush(heap, -arr[idx])
    return -1*heappop(heap)


# Average O(n), worst O(n**2)
def k_stat3(arr, position):

    assert position < len(arr)

    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]
        arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
        i = left
        j = right - 1
        while i < j:
            if arr[i] < pivot:
                i += 1
            elif arr[j] > pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if arr[i] >= pivot:
             arr[i], arr[right] = arr[right], arr[i]
             return i
        else:
            arr[i+1], arr[right] = arr[right], arr[i+1]
            return i+1

    def k_stat3_helper(left, right):
        idx = partition(left, right)
        if idx == position:
            return arr[position]
        elif idx > position:
            return k_stat3_helper(left, idx-1)
        else:
            return k_stat3_helper(idx + 1, right)

    return k_stat3_helper(0, len(arr)-1)
