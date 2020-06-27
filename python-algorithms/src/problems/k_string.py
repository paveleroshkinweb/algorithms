def k_string(n, line_number):
    total = 0
    for index_1 in range(1, n):
        if total <= line_number <= total + index_1:
            index_2 = line_number - total - 1
            break
        total += index_1
    res = ['a' if j not in [index_1, index_2] else 'b'
           for j in range(n - 1, -1, -1)
           ]
    return ''.join(res)


if __name__ == '__main__':
    results = ''
    for _ in range(int(input())):
        n, line_number = [int(e) for e in input().split()]
        results += k_string(n, line_number) + '\n'
    print(results, sep='')
