class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_idx = [0, 0]
        length = 0

        for i in range(1, len(s)-1):
            left = i-1
            right = i+1
            while left >= 0 and right <= len(s)-1:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            
            new_length = (right-1) - (left+1) + 1
            if new_length > length:
                length = new_length
                longest_idx = [left+1, right-1]

        for i in range(1, len(s)):
            left = i-1
            right = i
            while left >= 0 and right <= len(s)-1:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            
            new_length = (right-1) - (left+1) + 1
            if new_length > length:
                length = new_length
                longest_idx = [left+1, right-1]

        return s[longest_idx[0]:longest_idx[1]+1]
