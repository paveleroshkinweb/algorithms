def find_missing_number(n, numbers):
    total_sum = (n * (n + 1)) // 2
    subsum = sum(numbers)
    return total_sum - subsum


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    missing_number = find_missing_number(n, numbers)
    print(missing_number)
