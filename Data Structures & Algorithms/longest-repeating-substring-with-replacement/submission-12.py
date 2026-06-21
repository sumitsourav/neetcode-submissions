class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        max_so_far = 0
        max_window = 0
        left = 0
        for right in range(n):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            max_so_far = max(max_so_far, count[c])

            while (right - left + 1) - max_so_far > k:
                count[s[left]] = count[s[left]] - 1
                left = left + 1
            max_window = max(max_window, right - left + 1)
        return max_window