def find_member(f1, f2, n):
    solutions = [f1 - f2, f1, f2, f2 - f1, -f1, -f2, f1 - f2]
    return solutions[n % 6] % (10 ** 9 + 7)


if __name__ == '__main__':
    f1, f2 = [int(el) for el in input().split(' ')]
    n = int(input())
    print(find_member(f1, f2, n))