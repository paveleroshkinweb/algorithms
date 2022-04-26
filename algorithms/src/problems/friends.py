def get_array():
    arr = input().split(' ')
    return [int(el) for el in arr]


def get_max_happiness(numbers, friends_capacity):
    numbers = sorted(numbers, reverse=True)
    friends_capacity = sorted(friends_capacity)
    left = 0
    total_happiness = 0
    for friend_capacity in friends_capacity:
        if friend_capacity == 1:
            total_happiness += numbers[left] * 2
            left += 1
        elif friend_capacity == 2:
            total_happiness += numbers[left] + numbers[left + 1]
            left += 2
        else:
            total_happiness += numbers[left]
            left += 1
    for friend_capacity in friends_capacity:
        if friend_capacity > 2:
            total_happiness += numbers[left + friend_capacity - 2]
            left += friend_capacity - 1
    return total_happiness


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _ = get_array()
        numbers = get_array()
        friends_capacity = get_array()
        results.append(str(get_max_happiness(numbers, friends_capacity)))
    print('\n'.join(results))
