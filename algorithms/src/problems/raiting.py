def raiting(n):
    rait = 0
    bit_string = bin(n).replace('0b', '')
    for idx, bit in enumerate(bit_string):
        if bit == '1':
            rait += (2 ** (len(bit_string) - idx)) - 1
    return rait


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        results.append(
            str(raiting(int(input())))
        )
    print("\n".join(results))
