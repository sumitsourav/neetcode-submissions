class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        n = len(nums)
        freq = {}
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        max_heap = []

        for key, value in freq.items():
            heapq.heappush(max_heap, (-value, key))

        output = []
        while k > 0:
            output.append(heapq.heappop(max_heap)[1])
            k -= 1
        return output