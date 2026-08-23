class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        q = deque()
        time = 0

        counter = Counter(tasks)

        maxHeap = [count for count in counter.values()]
        heapq.heapify_max(maxHeap)


        while maxHeap or q:
            time += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count: q.append([count, time + n])
            elif q:
                time = q[0][1]

            if q and time == q[0][1]:
                val = q.popleft()[0]
                heapq.heappush_max(maxHeap, val)
        
        return time