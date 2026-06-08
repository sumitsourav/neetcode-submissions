class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = {}
        res = 0
        left = 0
        for right in range(len(s)):
            if s[right] in charset and charset[s[right]] >= left:
                left = charset[s[right]] + 1
            charset[s[right]] = right
            res = max(res, right - left + 1)
        return res
            
