class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(heap)
        return [[x, y] for _, x, y in (heapq.heappop(heap) for _ in range(k))]