class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search between speed 1 and max(piles)
        left, right = 1, max(piles)
        # Function to calculate the number of hours required
        while left < right:
            hours = 0
            mid = (left + right) // 2

            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return right

