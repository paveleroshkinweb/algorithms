def count_happy_people(times):
    passed = 0
    sorted_times = sorted(times)
    count = 0
    for time in sorted_times:
        if passed <= time:
            count += 1
            passed += time
    return count


if __name__ == '__main__':
    _ = input()
    times = [int(el) for el in input().split(' ')]
    print(count_happy_people(times))