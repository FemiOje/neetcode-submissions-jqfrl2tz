class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.maxHeap and num < self.maxHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, num)

        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                rem = heapq.heappop(self.minHeap)
                heapq.heappush_max(self.maxHeap, rem)
            else:
                rem = heapq.heappop_max(self.maxHeap)
                heapq.heappush(self.minHeap, rem)
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap): return self.minHeap[0]
        if len(self.minHeap) < len(self.maxHeap): return self.maxHeap[0]
        return (self.minHeap[0] + self.maxHeap[0]) / 2
        
        