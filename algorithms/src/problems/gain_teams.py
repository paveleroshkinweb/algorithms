import math
from collections import defaultdict


def find_teams(weights, x):
    weights.sort()
    dp = defaultdict(lambda: float('-inf'))
    dp[len(weights)] = 0
    if weights[-1] >= x:
        dp[len(weights) - 1] = 1
    for i in reversed(range(len(weights) - 1)):
        dp[i] = max(1 + dp[i + math.ceil(x / weights[i])], dp[i+1])
    return dp[0] if dp[0] != float('-inf') else 0


if __name__ == '__main__':
    results = []
    for _ in range(int(input())):
        _, x = input().split(' ')
        weights = [int(e) for e in input().split(' ')]
        results.append(str(find_teams(weights, int(x))))
    print("\n".join(results))
