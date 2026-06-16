class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        rate = 0
        l, r = 1, max_rate
        ans = max_rate
        while l <= r:
            m = (r + l) // 2
            currTime = 0
            for b in piles:
                currTime = currTime + (b + m - 1) // m
            if currTime <= h:
                # ans = min(m, ans)
                r = m - 1
            elif currTime > h:
                l = m + 1
        return l
