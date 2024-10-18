
class HitCounter:

    def __init__(self):
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        left = 0
        right = len(self.hits) - 1

        target_timestamp = timestamp - 300

        while left <= right:
            mid_pointer = (left+right) // 2
            if self.hits[mid_pointer] <= target_timestamp:
                left = mid_pointer + 1
            else:
                right = mid_pointer - 1
        return len(self.hits) - left







        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)