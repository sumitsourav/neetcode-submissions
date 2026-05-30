class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       set_s = {}
       set_t = {}
       for char in s:
        set_s[char] = set_s.get(char, 0) + 1
       for char in t:
        set_t[char] = set_t.get(char, 0) + 1

       if set_s == set_t:
        return True
       else:
        return False
       
