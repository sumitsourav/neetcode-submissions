class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        res = float("inf")
        end = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - left + 1)
                total -= nums[left]
                left = left + 1
        return 0 if res == float("inf") else res
                

