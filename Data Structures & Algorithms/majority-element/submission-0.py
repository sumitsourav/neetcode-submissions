class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n//2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > majority:
                return num