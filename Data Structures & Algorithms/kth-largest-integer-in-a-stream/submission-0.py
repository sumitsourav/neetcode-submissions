import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heapMin = list(nums)
        heapq.heapify(self.heapMin)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapMin, val)
        while len(self.heapMin) > self.k:
            heapq.heappop(self.heapMin)
        return self.heapMin[0]

