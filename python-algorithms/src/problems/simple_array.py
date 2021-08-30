def can_be_sorted(arr):
    min_element = min(arr)
    sorted_arr = sorted(arr)
    for s, n in zip(sorted_arr, arr):
        if n % min_element != 0 and s != n:
            return "NO"
    return "YES"


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        arr = [int(el) for el in input().split(' ')]
        results.append(can_be_sorted(arr))
    print("\n".join(results))
