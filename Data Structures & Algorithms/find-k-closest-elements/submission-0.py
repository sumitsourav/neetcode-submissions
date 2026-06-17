class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        close_heap = []
        for num in arr:
            distance = abs(x - num)
            heapq.heappush(close_heap, (distance, num))
        output_heap = []
        output = []
        for i in range(k):
            heapq.heappush(output_heap, heapq.heappop(close_heap)[1])
        for i in range(k):
            output.append(heapq.heappop(output_heap))
        return output
