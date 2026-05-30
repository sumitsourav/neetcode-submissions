class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set(nums)
        smallest = float('inf')
        if 1 not in unique:
            return 1
        for num in nums:
            left = num - 1
            right = num + 1
            if right not in unique and right > 0:
                if smallest > right:
                    smallest = right
            if left not in unique and left > 0:
                if smallest > left:
                    smallest = left
        return smallest
            

                



