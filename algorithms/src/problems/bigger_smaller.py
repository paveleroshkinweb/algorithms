def find_sequence(arr):
    curr_min = float('inf')
    size = 0

    seq =  []

    for i in range(len(arr)):
        element = arr[i]
        if element >= size + 1 and curr_min >= size + 1:
            curr_min = min(curr_min, element)
            size += 1
        else:
            seq.append(size)
            size = 1
            curr_min = element

    diff = len(arr) - sum(seq)
    if diff != 0:
        seq.append(diff)

    return seq


if __name__ == '__main__':
    results = []

    for _ in range(int(input())):
        _ = input()
        arr = list(map(int, input().split()))
        seq = find_sequence(arr)
        
        results.append(str(len(seq)))
        results.append(' '.join(map(str,seq)))

    print('\n'.join(results))
