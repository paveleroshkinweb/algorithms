import math


def binomial_coefficient(n, k):
    coefficient = 1
    for i in range(n-k+1, n+1):
        coefficient *= i
    return coefficient // math.factorial(k)


# Count number of solutions for equation
# x1 + x2 + x3 + x4 + x5 + x6 = 20
# where 0 <= x <= 20
def count_solutions():
    total_solutions = binomial_coefficient(25, 5)
    bad_solutions = binomial_coefficient(16, 5) * 6
    intersections = binomial_coefficient(6, 2) * binomial_coefficient(7, 5)
    return total_solutions - bad_solutions + intersections