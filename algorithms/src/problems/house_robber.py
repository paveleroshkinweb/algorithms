class Solution1:
    def rob(self, nums: list[int]) -> int:
        subsum = [0, 0, 0]
        for i in range(len(nums)):
            subsum.append(nums[i] + max(subsum[i+1], subsum[i]))
        return max(subsum[-1], subsum[-2])


class Solution2:
    def rob(self, nums: list[int]) -> int:
        prev1 = 0
        prev2 = 0
        prev3 = 0

        for i in range(len(nums)):
            sol = nums[i] + max(prev1, prev2)
            prev1, prev2, prev3 = prev2, prev3, sol

        return max(prev3, prev2)
