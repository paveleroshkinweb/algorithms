def construct(number, i):
    return number[:i] + number[-1] + number[i + 1:-1] + number[i]


def max_even_number(number):
    last_digit = int(number[-1])
    possible = -1
    for i, digit in enumerate(number):
        n_digit = int(digit)
        if n_digit & 1 == 0:
            possible = i
            if n_digit < last_digit:
                return construct(number, i)
    if possible != -1:
        return construct(number, possible)
    return -1


if __name__ == '__main__':
    number = input()
    print(max_even_number(number))