def is_subsum_exist(arr, target):
    left = 0
    current_subsum = arr[0]

    for right in range(1, len(arr)):

        if current_subsum == target:
            return True        

        elif current_subsum > target:
            current_subsum -= arr[left]
            left += 1
        
        current_subsum += arr[right]

    return current_subsum == target
