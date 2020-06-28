from math import factorial


def probability(drazil_path, actual_path):
    drazil_end_point = calc_end_point(drazil_path)
    actual_end_point = calc_end_point(actual_path)
    count_q = actual_path.count('?')
    if count_q == 0:
        return float(drazil_end_point == actual_end_point)
    n_options = 2 ** count_q
    n_good_options = calc_successful_options(drazil_end_point, actual_end_point, count_q)
    return n_good_options / n_options


def calc_end_point(path):
    return sum([
        (1 if sign == '+' else -1) * (0.5 if sign in ['+', '-'] else 0)
        for sign in path
    ])


def calc_successful_options(drazil_end_point, actual_end_point, count_q):
    diff = abs(drazil_end_point - actual_end_point)
    number_of_dominant_sign = diff // 0.5
    if number_of_dominant_sign > count_q or (count_q - number_of_dominant_sign) % 2 != 0:
        return 0
    opt1 = number_of_dominant_sign + (count_q - number_of_dominant_sign) / 2
    opt2 = count_q - opt1
    return factorial(count_q) / (factorial(opt1) * factorial(opt2))


if __name__ == '__main__':
    drazil_path = input()
    actual_path = input()
    print(probability(drazil_path, actual_path))
