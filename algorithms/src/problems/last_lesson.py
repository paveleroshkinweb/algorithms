def min_nok(n):
    if n % 2 == 0:
        return f'{n//2} {n//2}'
    i = 3
    while i * i <= n:
        if n % i == 0:
            return f'{n//i} {n-(n//i)}'
        i += 1
    return f'1 {n-1}'


if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        res.append(min_nok(int(input())))
    print("\n".join(res))
