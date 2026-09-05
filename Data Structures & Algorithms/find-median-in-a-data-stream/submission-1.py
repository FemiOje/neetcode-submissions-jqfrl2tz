class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

        heapq.heapify_max(self.maxHeap)
        heapq.heapify(self.minHeap)
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush_max(self.maxHeap, self.minHeap[0])
                heapq.heappop(self.minHeap)
            else:
                heapq.heappush(self.minHeap, self.maxHeap[0])
                heapq.heappop_max(self.maxHeap)
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap): return self.minHeap[0]
        if len(self.minHeap) < len(self.maxHeap): return self.maxHeap[0]
        return (self.minHeap[0] + self.maxHeap[0]) / 2
        
        