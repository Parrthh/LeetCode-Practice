class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.store.get(key, [])
        left, right = 0, len(val) - 1
        while left <= right:
            mid = (left + right)//2
            if val[mid][1] <= timestamp:
                res = val[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)