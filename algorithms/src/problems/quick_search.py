def left_binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        middle = (left + right) // 2
        element = arr[middle]

        if element >= target:
            right = middle - 1
        else:
            left = middle + 1

    return left


def right_binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:

        middle = (left + right) // 2
        element = arr[middle]

        if element > target:
            right = middle - 1
        else:
            left = middle + 1

    return right



def find_ranges(arr, ranges):
    arr.sort()
    answers = []

    for left, right in ranges:
        left_idx = left_binary_search(arr, left)
        right_idx = right_binary_search(arr, right)
        ans = right_idx - left_idx + 1
        answers.append(ans)
    return answers


if __name__ == '__main__':

    _ = input()
    arr = list(map(int, input().split(' ')))
    ranges = []
    for _ in range(int(input())):
        
        ranges.append(
            tuple(map(int, input().split(' ')))
        )

    answers = find_ranges(arr, ranges)
    print(*map(str, answers))
