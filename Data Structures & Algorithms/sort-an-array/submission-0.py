class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq
        n = len(nums)
        result = [0] * n
        heapq.heapify(nums)
        for i in range(n):
            key = heapq.heappop(nums)
            result[i] = key
        return result

