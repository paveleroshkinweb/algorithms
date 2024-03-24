def find_repeated_seq(measurements, k):
    k = min(k, len(measurements))
    
    prev_elements = set(measurements[:k])

    if len(prev_elements) != k:
        return True

    for i in range(k, len(measurements)):
        element = measurements[i]
        if element in prev_elements:
            return True
        
        prev_elements.remove(measurements[i-k])
        prev_elements.add(element)

    return False


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    measurements = list(map(int, input().split()))

    is_repeat = find_repeated_seq(measurements, k)

    if is_repeat:
        print("YES")
    else:
        print("NO")
