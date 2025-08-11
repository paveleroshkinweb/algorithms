class Solution:

    overflow = (2**31 - 1) // 10

    def reverse(self, x: int) -> int:
        overflow = Solution.overflow
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        result = 0
        while x_abs:
            if result > overflow:
                return 0
            result = result * 10 + (x_abs % 10)
            x_abs //= 10
        return result * sign
