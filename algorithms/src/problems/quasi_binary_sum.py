def merge(number1, number2):
    for idx in range(1, min(len(number1), len(number2)) + 1):
        if number1[-idx] == number2[-idx] == '1':
            return None
    return str(int(number1) + int(number2))


def quasi_binary_sum(number):
    quasi_sum = []
    for idx, n in enumerate(reversed(number)):
        quasi_sum.extend([str(10 ** idx)] * int(n))
    used = [True] * len(quasi_sum)
    for i in range(len(quasi_sum)):
        for j in range(i+1, len(quasi_sum)):
            merged_number = merge(quasi_sum[i], quasi_sum[j])
            if merged_number:
                used[i] = False
                quasi_sum[j] = merged_number
                break
    return [quasi_sum[idx] for idx in range(len(quasi_sum)) if used[idx]]


if __name__ == '__main__':
    number = input()
    quasi_sum = quasi_binary_sum(number)
    print(len(quasi_sum))
    print(' '.join(quasi_sum))
