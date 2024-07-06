def cont_subsum1(arr: list[int], target: int):
    # arr consists of positive sorted integers
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1
    subsum = sum(arr)

    while left < len(arr):

        if subsum == target:
            return True

        if subsum > target:
            subsum -= arr[right]
            right -= 1
        else:
            subsum -= arr[left]
            left += 1
    
    return False
