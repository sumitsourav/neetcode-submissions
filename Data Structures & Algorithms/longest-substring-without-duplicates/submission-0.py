class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        n = len(s)
        res = 0
        for i in range(n):
            charset = set()
            for j in range(i,n):
                if s[j] in charset:
                    break
                charset.add(s[j])
            res = max(res, len(charset))
        return res