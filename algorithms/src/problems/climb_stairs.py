class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev1 = 0
        prev2 = 0
        for price in cost:
            sol = price + min(prev1, prev2)
            prev1, prev2 = prev2, sol
        return min(prev1, prev2)
