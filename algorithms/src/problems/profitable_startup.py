def split_profit(n, k, d):
    if n % k == 0:
        return str(n) + ('0' * d)

    profit = -1

    for i in range(0, 10):
        profit = n * 10 + i
        if profit % k == 0:
            break
    else:
        return str(-1)

    return str(profit) + ('0' * (d-1))


if __name__ == '__main__':
    n, k, d = list(map(int, input().split()))
    splitted_profit = split_profit(n, k, d)
    print(splitted_profit)
