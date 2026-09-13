class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heapq.heappush(self.minheap, num)
        else:
            if num >= self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + -self.maxheap[0]) / 2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]