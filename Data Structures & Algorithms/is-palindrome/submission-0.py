class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = s.replace(" ", "").lower()
        n = len(result)
        l = 0
        r = n - 1
        res = True
        while l < r:
            if not result[l].isalnum():
                l = l + 1
                continue
            if not result[r].isalnum():
                r = r - 1
                continue
            if result[l] == result[r]:
                l = l + 1
                r = r - 1
            else:
                res = False
                break
        return res



        