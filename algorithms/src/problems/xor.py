def triple_xor(number):
    pairs = [[(0, 0), (1, 0), (1, 1)], [(0, 0), (0, 1), (0, 2)]]
    first_number = second_number = '1'
    max_obtained = 0
    for i in number[1:]:
        pair = pairs[max_obtained]
        first_number += str(pair[i][0])
        second_number += str(pair[i][1])
        max_obtained = max_obtained or int(pair[i][0] - pair[i][1] == 1)
    return first_number, second_number


if __name__ == '__main__':
    count_numbers = int(input())
    numbers = []
    for _ in range(count_numbers):
        _ = input()
        numbers.append([int(s) for s in list(input())])
    results = ['\n'.join(triple_xor(n)) for n in numbers]
    print('\n'.join(results), sep='')

