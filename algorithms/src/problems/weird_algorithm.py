def weird_algo(n):

    while n != 1:
        yield n

        if n & 1 == 0:
            n >>= 1

        else:
            n = n*3 + 1
    
    yield 1


if __name__ == '__main__':
    n = int(input())
    print(*map(str, weird_algo(n)))
