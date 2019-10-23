def calculate_pi():
    pi = 0
    current_denominator = 1
    sign = 1
    for i in range(0, 1000):
        pi += sign * (4 / current_denominator)
        sign *= -1
        current_denominator += 2
    return pi