def quick_sort(arr):
    copy = arr[:]
    do_sort(copy, 0, len(copy) - 1)
    return copy


def do_sort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    left_pointer = left
    right_pointer = right
    while left_pointer <= right_pointer:
        while left_pointer <= right_pointer and arr[left_pointer] < pivot:
            left_pointer += 1
        while left_pointer <= right_pointer and arr[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer <= right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1
            right_pointer -= 1
    do_sort(arr, left, right_pointer)
    do_sort(arr, left_pointer, right)
