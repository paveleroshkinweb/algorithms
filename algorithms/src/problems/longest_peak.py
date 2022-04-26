def longestPeak(array):
    if len(array) < 3:
        return 0
    max_peak = 0
    idx = 1
    while idx < len(array) - 1:
        peak = array[idx - 1] < array[idx] > array[idx + 1]
        if not peak:
            idx += 1
            continue
        left = idx - 1
        while left > 0 and array[left] > array[left - 1]:
            left -= 1
        right = idx + 1
        while right < len(array) - 1 and array[right] > array[right + 1]:
            right += 1
        max_peak = max(max_peak, right - left + 1)
        idx = right
    return max_peak
