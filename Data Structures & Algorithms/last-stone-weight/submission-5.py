class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapMax = []
        for n in stones:
            heapq.heappush(heapMax, -n)
        while len(heapMax) > 1:
            stone1 = abs(heapq.heappop(heapMax))
            stone2 = abs(heapq.heappop(heapMax))
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(heapMax, -(stone1 - stone2))
            else:
                heapq.heappush(heapMax, -(stone2 - stone1))
        return abs(heapMax[0]) if heapMax else 0