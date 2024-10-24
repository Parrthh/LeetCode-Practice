class MedianFinder:

    def __init__(self):
        # In python, these are members of the object, therefore self as prefix
        # Two heap: Small and Large
        self.small = []             # Small heap -> maxHeap
        self.large = []             # Large heap -> minHeap
                                    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # Make sure every element in small heap is <= element in large heap
        if (self.small and self.large and 
        (-1 * self.small[0]) > self.large[0]):
        # If the first element in small heap is greater than the first element in large heap
            val = -1 * heapq.heappop(self.small)# Since the value for maxHeap (small) are stored in negative format
            heapq.heappush(self.large, val)# While pushing into large heap we revert the negative to positive

        # If the size of the heap is uneven? We want the size of both the heap to atmost differ by 1 and not more
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)        
        
    def findMedian(self) -> float:
        # Calculating the median for two cases: If the lenght is uneven that means we have odd count of elements
        # Odd Count of elements:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # Even count of elements:
        return (-1 * self.small[0] + self.large[0]) / 2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()