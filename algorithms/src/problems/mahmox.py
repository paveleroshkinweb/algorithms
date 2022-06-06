def sequences(n, k):
    subsequences = [[1] + [0] * (k-1) for _ in range(n)]
    for number in range(1, n+1):
        for j in range(number, n+1, number):
            for i in range(1, k):
                subsequences[j-1][i] += subsequences[number-1][i-1]
    return sum(subsequences[i][-1] for i in range(n))


if __name__ == '__main__':
    n, k = input().split(' ')
    _sequences = sequences(int(n), int(k))
    print(_sequences % 1000000007)
