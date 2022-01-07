def arrayOfProducts(array):
    cache_left = []
    current_mul = 1
    for element in array:
        cache_left.append(current_mul)
        current_mul *= element

    cache_right = [0 for _ in range(len(array))]
    current_mul = 1
    for i in range(len(array) - 1, -1, -1):
        cache_right[i] = current_mul
        current_mul *= array[i]

    return [cache_left[i] * cache_right[i] for i in range(len(array))]