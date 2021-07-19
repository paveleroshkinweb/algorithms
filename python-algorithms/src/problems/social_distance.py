import math


def get_gaps(binary_str, k):
    gaps = []
    prev = -1
    for i, bit in enumerate(binary_str):
        if bit == '1':
            diff = i - prev - 1
            if prev == -1:
                diff += k
            gaps.append(diff)
            prev = i
    if prev != len(binary_str) - 1:
        if prev == -1:
            gaps.append(len(binary_str) + 2*k)
        else:
            gaps.append(len(binary_str) - prev - 1 + k)
    return gaps


def count_inversions(binary_str, k):
    gaps = get_gaps(binary_str, k)
    count = 0
    for gap in gaps:
        if gap >= 2 * k + 1:
            count += math.ceil((gap - 2*k) / (k+1))
    return count


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        n, k = [int(e) for e in input().split(' ')]
        binary_str = input()
        results.append(str(count_inversions(binary_str, k)))
    print("\n".join(results))