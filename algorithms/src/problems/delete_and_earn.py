from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        counter_map = Counter(nums)
        unique_numbers = sorted(list(counter_map))
        prev1 = 0
        prev2 = 0
        prev3 = unique_numbers[0] * counter_map[unique_numbers[0]]

        for idx in range(1, len(unique_numbers)):
            sol = unique_numbers[idx] * counter_map[unique_numbers[idx]]
            if unique_numbers[idx] == unique_numbers[idx-1] + 1:
                sol += max(prev1, prev2)
            else:
                sol += max(prev2, prev3)
            prev1, prev2, prev3 = prev2, prev3, sol
        return max(prev2, prev3)
