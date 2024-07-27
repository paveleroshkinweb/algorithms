import math


# find a solution for equation if it's possible with binary search
def solve(target, *, function, iterations, delta=0.001):
    left = 0
    right = target

    for _ in range(iterations):
        middle = (left + right) / 2
        solution = function(middle)

        if abs(solution - target) <= delta:
            return middle
        elif solution > target:
            right = middle
        else:
            left = middle

    return solution
