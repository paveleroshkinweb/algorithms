def max_drazil_factorial(digits):
    digits = [digit for digit in digits if digit not in [0, 1]]
    result = []
    map = {
        4: [2, 2, 3],
        6: [3, 5],
        8: [2, 2, 2, 7],
        9: [7, 3, 3, 2]
    }
    for digit in digits:
        if digit in map:
            result += map[digit]
        else:
            result.append(digit)
    return ''.join([str(el) for el in reversed(sorted(result))])


if __name__ == '__main__':
    _ = input()
    digits = [int(el) for el in list(input())]
    print(max_drazil_factorial(digits))
