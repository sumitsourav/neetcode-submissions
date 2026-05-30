class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_product = [1] * length
        postfix_product = [1] * length

        output = [1] * length

        for i in range(1, length):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        for i in range((length - 2), -1, -1):
            postfix_product[i] = postfix_product[i + 1] * nums[i + 1]

        for i in range(length):
            output[i] = prefix_product[i] * postfix_product[i]
        
        return output