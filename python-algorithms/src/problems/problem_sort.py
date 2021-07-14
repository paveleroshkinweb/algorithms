def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True


def is_homogeneous(mask):
    ones = len([bit for bit in mask if bit == 1])
    return ones == len(mask) or ones == 0


def is_sortable(arr, mask):
    if is_sorted(arr) or not is_homogeneous(mask):
        return "YES"
    return "NO"


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = input()
        arr = [int(n) for n in input().split()]
        mask = [int(n) for n in input().split()]
        results.append(is_sortable(arr, mask))
    print("\n".join(results))
