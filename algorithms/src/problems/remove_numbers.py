from collections import Counter

def remove_min_numbers(numbers):
    c = Counter(numbers)
    min_numbers = len(numbers)

    for n in c:
        prev = c[n-1]
        min_numbers = min(min_numbers, len(numbers) - prev - c[n])

    return min_numbers


if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split()))
    removed_count = remove_min_numbers(numbers)
    print(removed_count)
