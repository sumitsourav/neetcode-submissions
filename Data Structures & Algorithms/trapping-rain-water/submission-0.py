class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        leftmax, rightmax = height[left], height[right]
        count = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    count = count + leftmax - height[left]
            else:
                right -= 1
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    count = count + rightmax - height[right]
        return count

