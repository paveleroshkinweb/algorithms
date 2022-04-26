def find_length_sum_digits(m, s):
    if m * 9 < s or s == 0 and m != 1:
        return '-1 -1'
    min_n = find_min(m, s)
    max_n = find_max(m, s)
    return min_n + ' ' + max_n


def find_min(m, s):
    min_n = ''
    length = m - 1
    while length != 0:
        for i in range(9, -1, -1):
            if 1 <= s - i <= 9 * length:
                s -= i
                min_n = str(i) + min_n
                break
        length -= 1
    min_n = str(s) + min_n
    return min_n


def find_max(m, s):
    max_n = ''
    for i in range(0, m):
        diff = min(s, 9)
        s -= diff
        max_n += str(diff)
    return max_n


if __name__ == '__main__':
    m, s = [int(e) for e in input().split()]
    print(find_length_sum_digits(m, s))