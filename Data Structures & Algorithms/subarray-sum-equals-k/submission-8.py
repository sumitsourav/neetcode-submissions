class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0
        current_sum = 0

        for num in nums:
            current_sum = current_sum + num
            if (current_sum - k) in prefix_sum:
                count = count + prefix_sum[current_sum - k]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count