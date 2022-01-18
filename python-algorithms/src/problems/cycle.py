def hasSingleCycle(array):
    visited = 0
    current_idx = 0
    while visited < len(array):
        if visited > 0 and current_idx == 0:
            return False
        visited += 1
        current_idx = next_idx(current_idx, array)
    return current_idx == 0


def next_idx(idx, array):
    current_element = array[idx]
    next_idx = (current_element + idx) % len(array)
    return int(next_idx)
