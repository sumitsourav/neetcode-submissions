class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counts = {}
        max_so_far = 0
        left = 0
        max_window = 0
        for right in range(n):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            max_so_far = max(max_so_far, counts[char])

            while (right - left + 1) - max_so_far > k:
                counts[s[left]] = counts[s[left]] - 1
                left = left + 1
            max_window = max(max_window, (right - left + 1))
        return(max_window)

