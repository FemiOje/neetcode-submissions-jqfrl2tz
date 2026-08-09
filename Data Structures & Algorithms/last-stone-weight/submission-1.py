class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        maxHeap = stones

        while len(stones) > 1:
            diff = heapq.heappop_max(maxHeap) - heapq.heappop_max(maxHeap)
            if diff > 0: heapq.heappush_max(maxHeap, diff)

        return maxHeap[0] if len(maxHeap) > 0 else 0
