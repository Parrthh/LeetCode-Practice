class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.streams = nums
        self.streams.sort()
        

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.streams.insert(index, val)
        return self.streams[-self.k]

    
    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.streams) - 1
        while left <= right:
            mid = (left+right)//2
            mid_element = self.streams[mid]
            if mid_element == val:
                return mid
            elif mid_element > val:
                right = mid - 1
            else:
                left = mid + 1
        return left
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)