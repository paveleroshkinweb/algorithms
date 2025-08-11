class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lettersMap = {}
        lIdx = 0
        best = 0
        for i in range(len(s)):
            prevIdx = lettersMap.get(s[i], -1)
            if prevIdx >= lIdx:
                best = max(best, i - lIdx)
                lIdx = prevIdx + 1
            lettersMap[s[i]] = i
        return max(best, len(s) - lIdx)
