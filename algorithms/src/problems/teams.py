def teams(n, m):
    if n - m > 1 or m > (n+1) * 2:
        return -1
    prev_zero = False
    ones_row = 0
    zero_count = 0
    ones_count = 0
    total_length = n + m
    bit_string = [None for _ in range(total_length)]
    for i in range(total_length):
        if prev_zero:
            bit_string[i] = '1'
            ones_count += 1
            ones_row += 1
            prev_zero = False
        elif ones_row == 2:
            bit_string[i] = '0'
            zero_count += 1
            prev_zero = True
            ones_row = 0
        elif m - ones_count >= n - zero_count:
            bit_string[i] = '1'
            ones_count += 1
            ones_row += 1
            prev_zero = False
        else:
            bit_string[i] = '0'
            zero_count += 1
            prev_zero = True
            ones_row = 0
    return "".join(bit_string)


if __name__ == '__main__':
    n, m = input().split(' ')
    print(teams(int(n), int(m)))