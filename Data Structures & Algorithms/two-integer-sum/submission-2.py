class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup and i != lookup[complement]:
                return [i,lookup[complement]] 