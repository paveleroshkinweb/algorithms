def find_operations(numbers):
    current_parity = numbers[0] & 1
    signs = []
    for i in range(1, len(numbers)):
        next_n = numbers[i]
        next_parity = next_n & 1
    
        if current_parity == 0 and next_parity == 0:
            signs.append('+')
            continue

        elif current_parity == 0 and next_parity == 1:
            signs.append('+')
        elif current_parity == 1 and next_parity == 0:
            signs.append('+')
        else:
            signs.append('x')

        current_parity = 1
    return ''.join(signs)


if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split()))
    operations = find_operations(numbers)
    print(operations)
