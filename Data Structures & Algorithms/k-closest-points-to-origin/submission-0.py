from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapMin = []
        origin = (0,0)
        for x, y in points:
            distance = sqrt((origin[0] - x)**2 + (origin[1] - y)**2)
            heapq.heappush(heapMin, (distance, (x,y)))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heapMin)[1])
        return result